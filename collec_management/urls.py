from django.urls import path

from . import views 

urlpatterns = [
    path('about/',views.about,name = 'about'),
    path('collec_infos/<int:n>',views.collec_infos,name='collecinfos'),
    path('all/',views.collec_list,name='collec_list')
]