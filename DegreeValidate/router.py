from rest_framework import routers

from aplic.api.viewsets import *

router = routers.DefaultRouter()
router.register('alunos', AlunoViewSet)
router.register('atividades-complementares', AtividadeComplementarViewSet)
router.register('campus', CampusViewSet)
router.register('categorias-atividades-complementares', CategoriaAtividadeComplementarViewSet)
router.register('empresa', EmpresaViewSet)
router.register('instituicoes', InstituicaoViewSet)
router.register('usuarios', UsuarioViewSet)
