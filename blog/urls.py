from django.urls import path
from .views import ArticleList, Articledetail, categoryList, authorList, ArticlePreview, SearchList

app_name = "blog"
urlpatterns = [
    path('', ArticleList.as_view(), name="home"),
    path('page/<int:page>', ArticleList.as_view(), name="home"),
    path('article/<slug:slug>', Articledetail.as_view(), name="more"),
    path('category/<slug:slug>', categoryList.as_view(), name="category"),
    path('category/<slug:slug>/page/<int:page>', categoryList.as_view(), name="category"),
    path('author/<slug:username>', authorList.as_view(), name="author"),
    path('author/<slug:username>/page/<int:page>', authorList.as_view(), name="author"),
    path('preview/<int:pk>', ArticlePreview.as_view(), name="preview"),
    path('search/page/<int:page>', SearchList.as_view(), name="search"),
    path('search/', SearchList.as_view(), name="search"),
]
