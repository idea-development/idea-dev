# Class base view
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import PostForm, EditForm

# Create your views here.


class ArticlesView(ListView):
    model = Post
    template_name = 'articles.html'

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