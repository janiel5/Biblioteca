from django.contrib import admin

from .models import *

class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'matricula', 'data_nascimento')

class EmprestismoAdmin(admin.ModelAdmin):
    list_dislay = ('data_devolução','data_retirada', 'aluno', 'devolvido')

admin.site.register(Livro)
admin.site.register(Autor)
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Emprestismo, EmprestismoAdmin)
# Register your models here.
