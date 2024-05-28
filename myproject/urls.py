from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('explore/', views.explore, name='explore'),
    path('upgrade/', views.upgrade, name='upgrade'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('route/<int:route_id>/', views.route_detail, name='route_detail'),
    path('plan_trail/', views.plan_trail, name='plan_trail'),
    path('upload_trail/', views.upload_trail, name='upload_trail'),
    path('your_trails/', views.your_trails, name='your_trails'),
    path('download/', views.download, name='download'),
    path('about/', views.about, name='about'),
    path('donors/', views.donors, name='donors'),
    path('team/', views.team, name='team'),
]

