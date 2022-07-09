from calendar import firstweekday
from django.shortcuts import render
# Class base view
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm

# Create your views here.


class ArticlesView(ListView):
    model = Post
    template_name = 'articles.html'

class ArticleView(DetailView):
    model = Post
    template_name = 'article.html'

class AddArticleView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_article.html'
    # fields = '__all__'
    # fields  = [
    #     'title',
    #     'title_tag',
    #     'author',
    #     'body',
    # ]