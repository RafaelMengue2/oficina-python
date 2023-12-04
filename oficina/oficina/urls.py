from django.contrib import admin
from django.urls import path
from app1 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
    
    path('home/',views.HomePage, name='home'),
    path('addcar/', views.AddCarPage, name="addcar"),
    path('editcar/', EditCarPage, name="editcar"),
    path('deletecar/', views.DeleteCar, name="deletecar"),
    
    path('pecas/', views.PecaPage, name="pecas"),
    path('addpecas/', views.AddPecaPage, name="addpecas"),
    
    path('servicos/', views.ServicoPage, name="servicos"),
    path('addservicos/', views.AddServicoPage, name="addservicos"),
    
    path('clientes/', views.ClientePage, name="cliente"),
    path('addclientes/', views.AddClientePage, name="addclientes"),
 
]
