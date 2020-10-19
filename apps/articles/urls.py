from django.urls import path
from . import views
app_name = 'articles'
urlpatterns = [
    # path('', views.index, name='list'),
    # path('myview/', views.MyView.as_view(), name='view'),
    path('', views.ArticleView.as_view(), name='list'),
    path('<int:pk>/<slug:slug>', views.ArticleDetailView.as_view(), name='detail'),
    path('article-update/<int:pk>/<slug:slug>', views.ArticleUpdateView.as_view(), name='update'),
    path('article-delete/<int:pk>/<slug:slug>', views.ArticleDeleteView.as_view(), name='delete'),
    path('article-comment/<int:pk>/<slug:slug>', views.CommentCreateView.as_view(), name='comment'),
    path('article-create', views.ArticleCreateView.as_view(), name='create'),
    # path('<int:pk>/<str:slug>/', views.ArticleDetailView.as_view(), name='detail'),
]
