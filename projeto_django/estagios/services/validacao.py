from ..models import (
    TipoDocumento,
    StatusSolicitacao,
    Pendencia,
    TipoPendencia
)
from decimal import Decimal

def validar_solicitacao(solicitacao):

    obrigatorios = {
        TipoDocumento.CONTRATO,
        TipoDocumento.TERMO_COMPROMISSO,
        TipoDocumento.APOLICE_SEGURO,
    }

    enviados = set(
        solicitacao.documentos.values_list(
            "tipo",
            flat=True
        )
    )

    faltando = obrigatorios - enviados

    solicitacao.pendencias.all().delete()

    if faltando:

        for doc in faltando:

            Pendencia.objects.create(
                solicitacao=solicitacao,
                tipo=TipoPendencia.DOCUMENTO_INVALIDO,
                descricao=f"Documento obrigatório ausente: {doc}"
            )

        solicitacao.status = StatusSolicitacao.COM_PENDENCIAS

    else:

        solicitacao.status = StatusSolicitacao.APROVADA
        solicitacao.score_conformidade = Decimal('100.00')

    solicitacao.save()

    return {
        "status": solicitacao.status,
        "score": solicitacao.score_conformidade,
        "faltando": list(faltando)
    
    }