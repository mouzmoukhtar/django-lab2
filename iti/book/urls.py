from django.urls import path
from book import views
urlpatterns = [
    path('all/', views.getallbooks),
    path('onebook/<bk_id>',views.getbook),
    path('new', views.newbook),
    path('edit/<bk_id>', views.editbook),
    path('delete/<bk_id>', views.deletebook),

]