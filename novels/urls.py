from django.urls import path
from .import views

urlpatterns = [
    path('',views.info,name='info'),
    path('<int:novel_id>',views.detail,name='detail')
]