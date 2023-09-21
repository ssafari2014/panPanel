from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list_View.as_view(), name='article-list-View'),
    path('cut/<str:category>', views.article_list_View.as_view(), name='article-list-category')

]