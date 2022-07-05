from django.urls import path
from .views import ArticlesView, ArticleView, AddArticleView

urlpatterns = [
    path('articles', ArticlesView.as_view(), name='articles'),
    path('article/<int:pk>', ArticleView.as_view(), name='article'),
    path('add-article', AddArticleView.as_view(), name='add_article'),
]
