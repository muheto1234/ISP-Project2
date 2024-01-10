"""
URL configuration for Multiple project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users.views import (directeur,users,update_roles,deconnexionUser,deconnexion,secraiteur,reponse_dir,dir_get_perm,connexionUser,
                         RegisterUser,deletePerm,update,cop_vue_reponse,all_reponse,Reponse,get_permission,compte,
                         commandant,add_user,sous_off,cops,register,connexion, resetPwd, ResetPWDPage)
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as Views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reset_password',Views.PasswordResetView.as_view(template_name='password_reset.html'),name='reset_password'),
    path('reset_password_send',Views.PasswordResetDoneView.as_view(template_name='password_reset_sent.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',Views.PasswordResetConfirmView.as_view(template_name='password_reset_form.html'),name='password_reset_confirm'),
    path('reset_password_complete',Views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'),name='password_reset_complete'),
    path('directeur/',directeur,name='directeur'),
    path('compte/',compte,name='compte'),
    path('users/',users,name='users'),
    path('update_roles/<int:id>/',update_roles,name='update_roles'),
    path('add_user/',add_user,name='add_user'),
    path('dir_get_perm/<int:id>',dir_get_perm,name='dir_get_perm'),
    path('commandant/',commandant,name='commandant'),
    path('secraiteur/',secraiteur,name='secraiteur'),
    path('reponse_dir/<int:id>',reponse_dir,name='reponse_dir'),
    path("",connexionUser,name='connexionUser'),
    path('deconnexionUser/',deconnexionUser,name='deconnexionUser'),
    path('deconnexion/',deconnexion,name='deconnexion'),
    path('User/Register/',RegisterUser,name='RegisterUser'),
    #path('demande_permission/',demande_permission,name='demande_permission'),
    path('Reponse/<str:matricule>',Reponse,name='Reponse'),
    path('deletePerm/<int:id>/',deletePerm,name='deletePerm'),
    path('get_permission/',get_permission,name='get_permission'),
    path('cops/',cops,name='cop'),
    path('update/<int:id>',update,name='update'),
    path('cop_vue_reponse/<str:matricule>/',cop_vue_reponse,name='cop_vue_reponse'),
    path('all_reponse/<int:id>/',all_reponse,name='all_reponse'),
    path('register/',register,name='register'),
    path('login/',connexion,name='login'),
    path('sous_off/',sous_off,name='sous_off'),
    path('reset/pwd/',resetPwd,name='restPWD'),
    path('reset-password/<str:matricule>/', ResetPWDPage, name='resetPWD_page'),
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
