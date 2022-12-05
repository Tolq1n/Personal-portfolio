from django.urls import path
from todoadpp import views
from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [
    path('home1/', views.home1, name='home1'),
    path('signup/', views.signupuser, name='signupuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('create/', views.createtodos, name='createtodos'),
    path('complate/', views.comptodos, name='comptodos'),
    path('current/', views.currenttodos, name='currenttodos'),
    path('view/<int:id>', views.viewtodos, name='viewtodos'),
    path('view/<int:id>/complate', views.complatetodos, name='complatetodos'),
    path('view/<int:id>/delete', views.deletetodos, name='deletetodos'),
]
