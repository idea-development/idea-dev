from django.urls import path
from .views import ArticlesView, ArticleView, AddArticleView, UpdateArticleView, DeleteArticleView

urlpatterns = [
    path('articles', ArticlesView.as_view(), name='articles'),
    path('article/<int:pk>', ArticleView.as_view(), name='article'),
    path('add-article', AddArticleView.as_view(), name='add_article'),
    path('article/edit/<int:pk>', UpdateArticleView.as_view(), name='update_article'),
    path('article/<int:pk>/delete', DeleteArticleView.as_view(), name='delete_article'),
]
