from django.urls import path
from . import views

urlpatterns=[ 
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('addpost/',views.addpost,name='addpost'),
    path('show/<int:id>',views.show,name='show'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('delete/<int:id>',views.delete,name='delete')
]