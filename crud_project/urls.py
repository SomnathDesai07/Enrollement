from django.contrib import admin
from django.urls import path,include
from enroll_app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.add_show_view,name='addandshow'),
    path("delete/<int:id>/", views.delete_data_view,name='deletedata'),
    path("<int:id>/", views.update_data_view,name='updatedata'),
    path('api/',include('enroll_app.api.urls'))
]
