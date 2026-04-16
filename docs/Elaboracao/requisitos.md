---
id: levantamento de requisitos
title: Levantamento de Requisitos
---
# **06 - Levantamento de Requisitos**

**Sistema:** Sistema para validar estágios

---

## **1. Identificação dos Stakeholders**

- **Professores:** Realizam a análise qualitativa dos relatórios de estágio, focando no desempenho acadêmico do aluno e na coerência entre as atividades desenvolvidas e os objetivos do curso, registrando avaliações e feedbacks no sistema.
- **Estudantes:** Quem solicita a validação do estágio.
- **Empresas parceiras:** Organizações que ofertam o estágio, fornecem informações contratuais e realizam assinaturas necessárias para validação.
- **Coordenação de estágio / coordenação de curso:** Responsáveis por supervisionar o processo automatizado, validar documentos, acompanhar indicadores, solicitar correções e validar exceções.

---

### **2. Requisitos Funcionais**

| ID   | Descrição                                                                    | Prioridade |
| ---- | ------------------------------------------------------------------------------ | ---------- |
| RF01 | O sistema deve validar automaticamente os dados submetidos com base nas regras da Lei 11.788/2008 e regulamentos institucionais, indicando inconsistências | Alta |
| RF02 | O sistema deve calcular e exibir um índice de conformidade para cada solicitação, com base nas validações realizadas. | Alta |
| RF03 | O sistema deve identificar automaticamente pendências e retornar ao aluno as correções necessárias, sem intervenção manual. | Alta |
| RF04 | O sistema deve permitir ao aluno submeter documentos obrigatórios de estágio (contrato, termo de compromisso e relatórios) por meio de uma interface estruturada. | Alta |
| RF05 | O sistema deve enviar notificações automáticas ao aluno sobre mudanças de status, pendências e prazos relacionados ao estágio. | Média |
| RF06 | O sistema deve permitir a visualização geral das solicitações por meio de um painel gerencial, com indicadores e status atualizados. | Média |
| RF07 | O sistema deve disponibilizar modelos padronizados de documentos exigidos pela instituição para apoio ao aluno. | Baixa |

### **3. Requisitos Não Funcionais**

- **Segurança:** O sistema deve garantir acesso apenas a usuários autenticados por meio de credenciais institucionais, assegurando a integridade e confidencialidade dos dados acadêmicos e contratuais.
- **Performance:** O processamento automático dos documentos e o cálculo do índice de conformidade devem ser executados em tempo reduzido, preferencialmente em até 15 segundos após o envio.
- **Disponibilidade:** O sistema deve permanecer acessível de forma contínua, suportando variações de carga e picos de utilização em períodos críticos do calendário acadêmico.
- **Confiabilidade:** O sistema deve registrar e manter um histórico consistente e auditável de todas as validações, decisões e interações realizadas.
- **Usabilidade::** A interface deve ser intuitiva, responsiva e adaptável a diferentes dispositivos, proporcionando navegação simples e visualização eficiente dos documentos submetidos.

---

## Autor(es)
| Data | Versão | Descrição | Autor(es) |
| -- | -- | -- | -- |
| 16/04/26 | 1.0 | Levantamento de requisitos. | Gabriel Barreto, Guilherme Braz, Ísis Tavares, Mariana Faria e Matheus Avarenga. | 
