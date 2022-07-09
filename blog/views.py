# Class base view
# from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

# Create your views here.


class ArticlesView(ListView):
    model = Post
    template_name = 'articles.html'
    # ordering = ['-pk']
    ordering = ['-publish_date']

class ArticleView(DetailView):
    model = Post
    template_name = 'article.html'

class AddArticleView(CreateView):
    model = Post
    template_name = 'add_article.html'
    form_class = PostForm

class UpdateArticleView(UpdateView):
    model = Post
    template_name = 'update_article.html'
    form_class = EditForm

class DeleteArticleView(DeleteView):
    model = Post
    template_name = 'delete_article.html'
    success_url = reverse_lazy('articles')