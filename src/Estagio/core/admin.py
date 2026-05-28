from django.contrib import admin
from .models import Conta, Perfil, Postagem, Interacao, Mensagem

admin.site.register(Conta)
admin.site.register(Perfil)
admin.site.register(Postagem)
admin.site.register(Interacao)
admin.site.register(Mensagem)
