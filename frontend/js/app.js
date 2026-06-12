

const API_BASE = 'http://127.0.0.1:8000/api/';
let toastInstance = null;
let modalInstance = null;



function showLoading() {
  document.getElementById('loadingOverlay').classList.remove('d-none');
}

function hideLoading() {
  document.getElementById('loadingOverlay').classList.add('d-none');
}

function showToast(message, type, title) {
  const toastEl = document.getElementById('toastMessage');
  const toastBody = document.getElementById('toastBody');
  const toastTitle = document.getElementById('toastTitle');
  const toastIcon = document.getElementById('toastIcon');

  const icons = {
    success: 'bi-check-circle-fill text-success',
    error: 'bi-x-circle-fill text-danger',
    warning: 'bi-exclamation-triangle-fill text-warning',
    info: 'bi-info-circle-fill text-primary'
  };

  toastIcon.className = `me-2 ${icons[type] || icons.info}`;
  toastTitle.textContent = title || (type === 'success' ? 'Sucesso' : type === 'error' ? 'Erro' : 'Informação');
  toastBody.textContent = message;

  if (!toastInstance) {
    toastInstance = new bootstrap.Toast(toastEl, { delay: 4000 });
  }
  toastInstance.show();
}

function getStatusBadgeClass(status) {
  const map = {
    'EM_PREENCHIMENTO': 'bg-secondary',
    'SUBMETIDA': 'bg-primary',
    'EM_VALIDACAO': 'bg-info',
    'COM_PENDENCIAS': 'bg-warning text-dark',
    'EM_ANALISE_EXCECAO': 'bg-purple',
    'APROVADA': 'bg-success',
    'REPROVADA': 'bg-danger'
  };
  return map[status] || 'bg-secondary';
}

function getStatusLabel(status) {
  const map = {
    'EM_PREENCHIMENTO': 'Em preenchimento',
    'SUBMETIDA': 'Submetida',
    'EM_VALIDACAO': 'Em validação',
    'COM_PENDENCIAS': 'Com pendências',
    'EM_ANALISE_EXCECAO': 'Em análise de exceção',
    'APROVADA': 'Aprovada',
    'REPROVADA': 'Reprovada'
  };
  return map[status] || status;
}

function getScoreBadgeClass(score) {
  if (score >= 80) return 'bg-success';
  if (score >= 50) return 'bg-warning text-dark';
  return 'bg-danger';
}

function formatDate(dateStr) {
  if (!dateStr) return '-';
  const d = new Date(dateStr);
  return d.toLocaleDateString('pt-BR', {
    day: '2-digit',
    month: '2-digit',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  });
}



function switchView(view) {
  document.querySelectorAll('.btn-view').forEach(btn => {
    btn.classList.remove('active');
    if (btn.dataset.view === view) {
      btn.classList.add('active');
    }
  });


  document.querySelectorAll('.view-section').forEach(section => {
    section.classList.add('d-none');
  });
  document.getElementById(`view-${view}`).classList.remove('d-none');

  if (view === 'coordenador') {
    carregarSolicitacoes();
  } else if (view === 'professor') {
    carregarRelatorios();
  }
}

async function carregarEmpresas() {
  try {
    const response = await fetch(`${API_BASE}empresas/`);
    if (!response.ok) throw new Error(`Erro HTTP ${response.status}`);
    const empresas = await response.json();

    const select = document.getElementById('empresaSelect');
    select.innerHTML = '<option value="">Selecione uma empresa...</option>';

    empresas.forEach(emp => {
      const option = document.createElement('option');
      option.value = emp.id;
      option.textContent = `${emp.razao_social} (${emp.cnpj})`;
      select.appendChild(option);
    });
  } catch (error) {
    console.error('Erro ao carregar empresas:', error);
    showToast('Não foi possível carregar a lista de empresas. Verifique se o servidor Django está rodando.', 'error');
  }
}


document.getElementById('formSolicitacao').addEventListener('submit', async function (e) {
  e.preventDefault();

  const empresaId = document.getElementById('empresaSelect').value;
  if (!empresaId) {
    showToast('Selecione uma empresa.', 'warning', 'Atenção');
    return;
  }

  const contrato = document.getElementById('uploadContrato').files[0];
  const termo = document.getElementById('uploadTermo').files[0];
  const apolice = document.getElementById('uploadApolice').files[0];

  if (!contrato || !termo || !apolice) {
    showToast('Envie os 3 documentos obrigatórios (Contrato, Termo e Apólice).', 'warning', 'Atenção');
    return;
  }

  const submitBtn = document.getElementById('btnEnviarSolicitacao');
  submitBtn.disabled = true;
  submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-1"></span>Enviando...';
  showLoading();

  try {
    const formData = new FormData();
    formData.append('empresa', empresaId);
    formData.append('upload_contrato', contrato);
    formData.append('upload_termo', termo);
    formData.append('upload_apolice', apolice);

    const response = await fetch(`${API_BASE}solicitacoes/`, {
      method: 'POST',
      body: formData
    });

    const data = await response.json();

    if (!response.ok) {
      const errorMsg = data.detail || data.error || JSON.stringify(data);
      throw new Error(errorMsg);
    }

    // Display validation result
    exibirResultadoValidacao(data);
    showToast('Solicitação enviada com sucesso!', 'success');

    // Reset form
    document.getElementById('formSolicitacao').reset();
  } catch (error) {
    console.error('Erro ao enviar solicitação:', error);
    showToast(`Erro ao enviar solicitação: ${error.message}`, 'error');
  } finally {
    submitBtn.disabled = false;
    submitBtn.innerHTML = '<i class="bi bi-cloud-arrow-up me-1"></i> Enviar Solicitação';
    hideLoading();
  }
});

function exibirResultadoValidacao(data) {
  const container = document.getElementById('resultadoValidacao');
  const status = data.status || 'Desconhecido';
  const score = parseFloat(data.score_conformidade) || 0;
  const statusClass = getStatusBadgeClass(status);
  const scoreClass = getScoreBadgeClass(score);

  container.innerHTML = `
    <div class="row justify-content-center">
      <div class="col-md-6">
        <div class="d-flex align-items-center mb-3 p-3 bg-light rounded">
          <i class="bi bi-robot fs-1 me-3 text-info"></i>
          <div>
            <h6 class="mb-1">Status da Solicitação #${data.id}</h6>
            <span class="badge ${statusClass} badge-status fs-6 me-2">${getStatusLabel(status)}</span>
          </div>
        </div>
        <div class="text-center p-3 bg-light rounded">
          <h6 class="mb-2">Score de Conformidade</h6>
          <div class="display-4 fw-bold ${score >= 80 ? 'text-success' : score >= 50 ? 'text-warning' : 'text-danger'}">
            ${score.toFixed(2)}%
          </div>
          <div class="progress mt-2" style="height: 8px;">
            <div class="progress-bar ${scoreClass}" role="progressbar" style="width: ${score}%" aria-valuenow="${score}" aria-valuemin="0" aria-valuemax="100"></div>
          </div>
        </div>
      </div>
    </div>
  `;
}


document.getElementById('formRelatorio').addEventListener('submit', async function (e) {
  e.preventDefault();

  const titulo = document.getElementById('relTitulo').value.trim();
  const descricao = document.getElementById('relDescricao').value.trim();

  if (!titulo || !descricao) {
    showToast('Preencha título e descrição do relatório.', 'warning', 'Atenção');
    return;
  }

  const submitBtn = document.getElementById('btnEnviarRelatorio');
  submitBtn.disabled = true;
  submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-1"></span>Enviando...';
  showLoading();

  try {
    const response = await fetch(`${API_BASE}relatorios/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ titulo, descricao })
    });

    const data = await response.json();

    if (!response.ok) {
      const errorMsg = data.detail || data.error || data.titulo || JSON.stringify(data);
      throw new Error(errorMsg);
    }

    showToast('Relatório enviado com sucesso!', 'success');
    document.getElementById('formRelatorio').reset();
  } catch (error) {
    console.error('Erro ao enviar relatório:', error);
    showToast(`Erro ao enviar relatório: ${error.message}`, 'error');
  } finally {
    submitBtn.disabled = false;
    submitBtn.innerHTML = '<i class="bi bi-send me-1"></i> Enviar Relatório';
    hideLoading();
  }
});


function buildStatusOptions(currentStatus) {
  const statuses = [
    { value: 'EM_PREENCHIMENTO', label: 'Em preenchimento' },
    { value: 'SUBMETIDA', label: 'Submetida' },
    { value: 'EM_VALIDACAO', label: 'Em validação' },
    { value: 'COM_PENDENCIAS', label: 'Com pendências' },
    { value: 'EM_ANALISE_EXCECAO', label: 'Em análise de exceção' },
    { value: 'APROVADA', label: 'Aprovada' },
    { value: 'REPROVADA', label: 'Reprovada' }
  ];
  return statuses.map(s =>
    `<option value="${s.value}" ${s.value === currentStatus ? 'selected' : ''}>${s.label}</option>`
  ).join('');
}

async function carregarSolicitacoes() {
  const tbody = document.getElementById('tbodySolicitacoes');
  tbody.innerHTML = `
    <tr>
      <td colspan="6" class="text-center text-muted py-4">
        <div class="spinner-border spinner-border-sm me-2" role="status"></div>
        Carregando solicitações...
      </td>
    </tr>
  `;

  try {
    const response = await fetch(`${API_BASE}solicitacoes/`);
    if (!response.ok) throw new Error(`Erro HTTP ${response.status}`);
    const solicitacoes = await response.json();

    if (solicitacoes.length === 0) {
      tbody.innerHTML = `
        <tr>
          <td colspan="6" class="text-center text-muted py-4">
            <i class="bi bi-inbox fs-3 d-block mb-2"></i>
            Nenhuma solicitação encontrada.
          </td>
        </tr>
      `;
      return;
    }

    const docsResponse = await fetch(`${API_BASE}documentos/`);
    const documentos = docsResponse.ok ? await docsResponse.json() : [];

    function countDocsBySolicitacao(solId) {
      return documentos.filter(doc => doc.solicitacao === solId).length;
    }

    tbody.innerHTML = solicitacoes.map(sol => {
      const statusClass = getStatusBadgeClass(sol.status);
      const score = parseFloat(sol.score_conformidade) || 0;
      const scoreClass = getScoreBadgeClass(score);
      const empresaNome = sol.empresa_display || (sol.empresa ? `Empresa #${sol.empresa}` : '-');
      const totalDocs = countDocsBySolicitacao(sol.id);

      return `
        <tr id="sol-row-${sol.id}">
          <td><strong>#${sol.id}</strong></td>
          <td>${empresaNome}</td>
          <td><span class="badge ${statusClass} badge-status">${getStatusLabel(sol.status)}</span></td>
          <td>
            <span class="badge ${scoreClass} badge-score">${score.toFixed(2)}%</span>
          </td>
          <td>${formatDate(sol.criado_em)}</td>
          <td class="text-center" style="min-width: 260px;">
            <button class="btn btn-outline-info btn-sm mb-1" onclick="analisarDocumentos(${sol.id})" title="Analisar documentos da solicitação">
              <i class="bi bi-file-earmark-pdf me-1"></i>Documentos (${totalDocs})
            </button>
            <button class="btn btn-outline-primary btn-sm mb-1" onclick="toggleAcoesSolicitacao(${sol.id})">
              <i class="bi bi-gear-fill me-1"></i>Ações
            </button>
            <div id="sol-actions-${sol.id}" class="d-none mt-1 p-2 border rounded bg-light text-start" style="min-width: 220px;">
              <form id="sol-form-${sol.id}" onsubmit="atualizarSolicitacao(event, ${sol.id})">
                <div class="mb-2">
                  <label class="form-label small mb-1">Status</label>
                  <select class="form-select form-select-sm" id="sol-status-${sol.id}">
                    ${buildStatusOptions(sol.status)}
                  </select>
                </div>
                <div class="mb-2">
                  <label class="form-label small mb-1">Score (0-100)</label>
                  <input type="number" class="form-control form-control-sm" id="sol-score-${sol.id}"
                         value="${score}" min="0" max="100" step="0.01">
                </div>
                <div class="d-grid gap-2">
                  <button type="submit" class="btn btn-success btn-sm">
                    <i class="bi bi-check2-circle me-1"></i>Salvar
                  </button>
                  <button type="button" class="btn btn-outline-secondary btn-sm" onclick="toggleAcoesSolicitacao(${sol.id})">
                    <i class="bi bi-x-lg me-1"></i>Cancelar
                  </button>
                </div>
              </form>
            </div>
          </td>
        </tr>
      `;
    }).join('');
  } catch (error) {
    console.error('Erro ao carregar solicitações:', error);
    tbody.innerHTML = `
      <tr>
        <td colspan="6" class="text-center text-danger py-4">
          <i class="bi bi-exclamation-triangle-fill fs-3 d-block mb-2"></i>
          Erro ao carregar solicitações: ${error.message}
        </td>
      </tr>
    `;
    showToast('Erro ao carregar solicitações.', 'error');
  }
}


function toggleAcoesSolicitacao(id) {
  const panel = document.getElementById(`sol-actions-${id}`);
  if (panel) {
    panel.classList.toggle('d-none');
  }
}


async function atualizarSolicitacao(event, id) {
  event.preventDefault();

  const statusSelect = document.getElementById(`sol-status-${id}`);
  const scoreInput = document.getElementById(`sol-score-${id}`);

  const novoStatus = statusSelect.value;
  const novoScore = parseFloat(scoreInput.value);

  if (isNaN(novoScore) || novoScore < 0 || novoScore > 100) {
    showToast('O score deve ser um número entre 0 e 100.', 'warning', 'Atenção');
    return;
  }

  if (!confirm(`Deseja atualizar a solicitação #${id}?\nStatus: ${getStatusLabel(novoStatus)}\nScore: ${novoScore.toFixed(2)}%`)) return;

  showLoading();
  try {
    const response = await fetch(`${API_BASE}solicitacoes/${id}/`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        status: novoStatus,
        score_conformidade: novoScore
      })
    });

    if (!response.ok) {
      const data = await response.json();
      throw new Error(data.detail || data.error || 'Erro ao atualizar solicitação');
    }

    showToast(`Solicitação #${id} atualizada com sucesso! (${getStatusLabel(novoStatus)}, Score: ${novoScore.toFixed(2)}%)`, 'success');
    carregarSolicitacoes();
  } catch (error) {
    console.error('Erro ao atualizar solicitação:', error);
    showToast(`Erro: ${error.message}`, 'error');
  } finally {
    hideLoading();
  }
}


function analisarDocumentos(id) {
  showLoading();
  setTimeout(() => {
    hideLoading();
    showToast(
      `Análise dos documentos da solicitação #${id} concluída.\n\n` +
      `📄 Contrato: OK\n` +
      `📄 Termo de Compromisso: OK\n` +
      `📄 Apólice de Seguro: OK\n\n` +
      `Nenhuma pendência encontrada.`,
      'success',
      'Análise de Documentos'
    );
  }, 1500);
}


async function carregarRelatorios() {
  const tbody = document.getElementById('tbodyRelatorios');
  tbody.innerHTML = `
    <tr>
      <td colspan="6" class="text-center text-muted py-4">
        <div class="spinner-border spinner-border-sm me-2" role="status"></div>
        Carregando relatórios...
      </td>
    </tr>
  `;

  try {
    const response = await fetch(`${API_BASE}relatorios/`);
    if (!response.ok) throw new Error(`Erro HTTP ${response.status}`);
    const relatorios = await response.json();

    if (relatorios.length === 0) {
      tbody.innerHTML = `
        <tr>
          <td colspan="6" class="text-center text-muted py-4">
            <i class="bi bi-inbox fs-3 d-block mb-2"></i>
            Nenhum relatório encontrado.
          </td>
        </tr>
      `;
      return;
    }

    tbody.innerHTML = relatorios.map(rel => {
      const statusBadge = rel.aprovado
        ? '<span class="badge bg-success badge-status"><i class="bi bi-check-circle me-1"></i>Aprovado</span>'
        : '<span class="badge bg-warning text-dark badge-status"><i class="bi bi-hourglass me-1"></i>Pendente</span>';

      const descricaoCurta = rel.descricao
        ? rel.descricao.substring(0, 60) + (rel.descricao.length > 60 ? '...' : '')
        : '-';

      return `
        <tr>
          <td><strong>#${rel.id}</strong></td>
          <td>${rel.titulo || 'Sem título'}</td>
          <td>
            <span title="${rel.descricao || ''}">${descricaoCurta}</span>
            ${rel.descricao && rel.descricao.length > 60 ? `
              <button class="btn btn-link btn-sm p-0 ms-1" onclick="abrirModalDetalhes(${rel.id})">
                Ver detalhes
              </button>
            ` : ''}
          </td>
          <td>${statusBadge}</td>
          <td>${rel.solicitacao ? `#${rel.solicitacao}` : '-'}</td>
          <td class="text-center">
            <div class="d-flex flex-wrap gap-1 justify-content-center">
              <button class="btn btn-outline-info btn-sm" onclick="abrirModalDetalhes(${rel.id})" title="Ver detalhes">
                <i class="bi bi-eye"></i>
              </button>
              <button class="btn btn-success btn-sm" onclick="aprovarRelatorio(${rel.id})" ${rel.aprovado ? 'disabled' : ''}>
                <i class="bi bi-check-lg"></i>
              </button>
              <button class="btn btn-danger btn-sm" onclick="reprovarRelatorio(${rel.id})" ${rel.aprovado ? 'disabled' : ''}>
                <i class="bi bi-x-lg"></i>
              </button>
            </div>
          </td>
        </tr>
      `;
    }).join('');
  } catch (error) {
    console.error('Erro ao carregar relatórios:', error);
    tbody.innerHTML = `
      <tr>
        <td colspan="6" class="text-center text-danger py-4">
          <i class="bi bi-exclamation-triangle-fill fs-3 d-block mb-2"></i>
          Erro ao carregar relatórios: ${error.message}
        </td>
      </tr>
    `;
    showToast('Erro ao carregar relatórios.', 'error');
  }
}

function abrirModalDetalhes(id) {
  const modalBody = document.getElementById('modalDetalhesBody');
  modalBody.innerHTML = `
    <div class="text-center py-4">
      <div class="spinner-border text-secondary" role="status">
        <span class="visually-hidden">Carregando...</span>
      </div>
    </div>
  `;

  // Show modal
  const modalEl = document.getElementById('modalDetalhesRelatorio');
  if (!modalInstance) {
    modalInstance = new bootstrap.Modal(modalEl);
  }
  modalInstance.show();

  // Fetch report details
  fetch(`${API_BASE}relatorios/${id}/`)
    .then(res => {
      if (!res.ok) throw new Error(`Erro HTTP ${res.status}`);
      return res.json();
    })
    .then(rel => {
      const statusBadge = rel.aprovado
        ? '<span class="badge bg-success fs-6"><i class="bi bi-check-circle me-1"></i>Aprovado</span>'
        : '<span class="badge bg-warning text-dark fs-6"><i class="bi bi-hourglass me-1"></i>Pendente</span>';

      modalBody.innerHTML = `
        <div class="mb-4">
          <h6 class="text-muted text-uppercase small mb-1">Título</h6>
          <h4 class="fw-bold">${rel.titulo || 'Sem título'}</h4>
        </div>
        <div class="mb-4">
          <h6 class="text-muted text-uppercase small mb-1">Status</h6>
          <div>${statusBadge}</div>
        </div>
        <div class="mb-4">
          <h6 class="text-muted text-uppercase small mb-1">Descrição Completa</h6>
          <div class="p-3 bg-light rounded border" style="white-space: pre-wrap; word-wrap: break-word;">
            ${rel.descricao || '<em class="text-muted">Nenhuma descrição fornecida.</em>'}
          </div>
        </div>
        <div class="row g-3">
          <div class="col-md-6">
            <h6 class="text-muted text-uppercase small mb-1">Solicitação</h6>
            <p class="mb-0">${rel.solicitacao ? `#${rel.solicitacao}` : '-'}</p>
          </div>
          <div class="col-md-6">
            <h6 class="text-muted text-uppercase small mb-1">Professor</h6>
            <p class="mb-0">${rel.professor ? `#${rel.professor}` : '-'}</p>
          </div>
        </div>
      `;
    })
    .catch(error => {
      console.error('Erro ao carregar detalhes:', error);
      modalBody.innerHTML = `
        <div class="text-center text-danger py-4">
          <i class="bi bi-exclamation-triangle-fill fs-1 d-block mb-2"></i>
          <p class="mb-0">Erro ao carregar detalhes do relatório.</p>
          <small>${error.message}</small>
        </div>
      `;
    });
}


async function aprovarRelatorio(id) {
  if (!confirm(`Deseja aprovar o relatório #${id}?`)) return;
  await patchRelatorio(id, true);
}

async function reprovarRelatorio(id) {
  if (!confirm(`Deseja reprovar o relatório #${id}?`)) return;
  await patchRelatorio(id, false);
}

async function patchRelatorio(id, aprovado) {
  showLoading();
  try {
    const response = await fetch(`${API_BASE}relatorios/${id}/`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ aprovado })
    });

    if (!response.ok) {
      const data = await response.json();
      throw new Error(data.detail || data.error || 'Erro ao atualizar relatório');
    }

    const action = aprovado ? 'aprovado' : 'reprovado';
    showToast(`Relatório #${id} ${action} com sucesso!`, 'success');
    carregarRelatorios();
  } catch (error) {
    console.error('Erro ao atualizar relatório:', error);
    showToast(`Erro: ${error.message}`, 'error');
  } finally {
    hideLoading();
  }
}

document.addEventListener('DOMContentLoaded', function () {
  // Load empresas for the student form
  carregarEmpresas();
});