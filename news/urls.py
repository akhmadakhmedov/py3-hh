from django.urls import path
from .views import *

urlpatterns = [
    path('list/', news_list, name='news-list'),
    path('detail/<int:id>/', news_detail, name='news-detail'),
    path("create/", NewsCreateView.as_view(), name='create-news'),
    path('update/<int:id>/', NewsUpdateView.as_view(), name='news-update'),

]