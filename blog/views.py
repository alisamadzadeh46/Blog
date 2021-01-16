from account.models import User
from django.shortcuts import get_object_or_404
from .models import Article, Category
from account.mixins import AccessMixin
from django.views.generic import ListView, DetailView
from django.db.models import Q
# def home(request, page=1):
#     articles_list = Article.objects.published()
#     pagintor = Paginator(articles_list, 3)
#     articles = pagintor.get_page(page)
#     context = {
#         "articles": articles,
#     }
#     return render(request, "blog/index.html", context)
class ArticleList(ListView):
    template_name = "blog/index.html"
    queryset = Article.objects.published()
    paginate_by = 3
    context_object_name = "articles"


# def more(request, slug):
#     context = {
#         "article": get_object_or_404(Article.objects.published(), slug=slug),
#     }
#     return render(request, "blog/article_detail.html", context)
class Articledetail(DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        article = get_object_or_404(Article.objects.published(), slug=slug)
        ipaddress = self.request.user.ipaddress
        if ipaddress not in article.hits.all():
            article.hits.add(ipaddress)
        return article


# def category(request, slug, page=1):
#     category = get_object_or_404(Category, slug=slug, status="True")
#     articles_list=category.articles.published()
#     pagintor = Paginator(articles_list, 3)
#     articles = pagintor.get_page(page)
#     context = {
#         "category": category,
#         "articles": articles,
#     }
#     return render(request, "blog/category.html", context)

class categoryList(ListView):
    paginate_by = 3
    template_name = "blog/category.html"

    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.active(), slug=slug)
        return category.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context


class authorList(ListView):
    paginate_by = 3
    template_name = "blog/author_list.html"

    def get_queryset(self):
        global author
        username = self.kwargs.get('username')
        author = get_object_or_404(User, username=username)
        return author.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = author
        return context


class ArticlePreview(AccessMixin, DetailView):
    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Article, pk=pk)


class SearchList(ListView):
    paginate_by = 3
    template_name = "blog/search_list.html"

    def get_queryset(self):
        search = self.request.GET.get('q')
        return Article.objects.filter(Q(description__icontains=search) | Q(title__icontains=search))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('q')
        return context
