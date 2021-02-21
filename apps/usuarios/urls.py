from django.urls import path

from apps.usuarios.views.view_login import LoginView,DashboarView,LogoutView,DashboardSinPrivilegio,\
    LineaView,BarraView,ResultadoView,PapeletaView

from apps.usuarios.views.view_usuario import UsuarioListarView,UsuarioCrearView,UsuarioEditarView,UsuarioEliminarView,UsuarioPerfilView

app_name = 'usuarios'

urlpatterns = [
    path('', LoginView.as_view(), name='index'),
    path('dashboard/', DashboarView.as_view(), name='dashboard'),
    path('perfil/<int:pk>/usuario/', UsuarioPerfilView.as_view(), name='usuario_perfil'),

    path('papeleta/', PapeletaView.as_view(), name='papeleta'),


    path('resultado/', ResultadoView.as_view(), name='resultado'),
    path('linea/', LineaView.as_view(), name='linea'),
    path('barra/', BarraView.as_view(), name='barra'),



    path('logout/', LogoutView, name='logout'),

    path('sin/privilegio/', DashboardSinPrivilegio.as_view(), name='sinprivilegio'),

    path('listar/usuario/', UsuarioListarView.as_view(), name='listar_usuario'),
    path('crear/usuario/', UsuarioCrearView.as_view(), name='crear_usuario'),
    path('editar/<int:pk>/usuario/', UsuarioEditarView.as_view(), name='editar_usuario'),
    path('eliminar/<int:pk>/usuario/', UsuarioEliminarView.as_view(), name='eliminar_usuario'),



]
#login/