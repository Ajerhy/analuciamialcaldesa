from django.urls import path

from apps.usuarios.views.view_login import LoginView,DashboarView,LogoutView,DashboardSinPrivilegio,\
    LineaView,BarraView,ResultadoView

from apps.usuarios.views.view_usuario import UsuarioListarView

app_name = 'usuarios'

urlpatterns = [
    path('', LoginView.as_view(), name='index'),
    path('dashboard/', DashboarView.as_view(), name='dashboard'),
    path('resultado/', ResultadoView.as_view(), name='resultado'),
    path('linea/', LineaView.as_view(), name='linea'),
    path('barra/', BarraView.as_view(), name='barra'),



    path('logout/', LogoutView, name='logout'),

    path('sin/privilegio/', DashboardSinPrivilegio.as_view(), name='sinprivilegio'),

    path('listar/usuario/', UsuarioListarView.as_view(), name='listar_usuario'),
]
#login/