from .views import *
from django.urls import path,include

urlpatterns = [
    path('home1/',home1,name='pg'),
    path('home/',home,name='pg1'),
    path('about/',about,name='pg2'),
    path('booking/',booking,name='pg3'),
    path('doctor/',doctor_list,name='pg4'),
    path('department/',department,name='pg5'),
    path('contact/',contact,name='pg6'),
    path('doctor/<slug:dept_slug>/',doctor_list,name='doctor_list_by_dept'),
    path('doctor/<slug:slug>/',doctor,name='doctor_detail'),

    path('department/',Tasklistview.as_view(),name='pg5'),
    path('deptdetail/<int:pk>',TaskDetailview.as_view(),name="cbdetail"),
    path('deptupdate/<int:pk>',TaskUpdateView.as_view(),name="deptupdates"),
    path('deptdelete/<int:pk>',TaskDeleteView.as_view(),name="deptdelete"),
    path('deptcreate/',TaskCreateView.as_view(),name='deptcreate'),

    path('',login,name='login'),
    path('logout/',logout,name='logout')
]
