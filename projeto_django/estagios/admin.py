from django.contrib import admin
from .models import *

admin.site.register(Usuario)
admin.site.register(EmpresaParceira)
admin.site.register(SupervisorEmpresa)
admin.site.register(SolicitacaoEstagio)
admin.site.register(ModeloDocumento)
admin.site.register(Documento)
admin.site.register(RelatorioEstagio)
admin.site.register(Assinatura)
admin.site.register(Pendencia)
admin.site.register(AnaliseExcecao)
admin.site.register(Notificacao)