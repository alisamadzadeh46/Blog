from django.db import models
from account.models import User
from django.utils import timezone
from django.urls import reverse
from django.utils.html import format_html
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment
from extensions.util import jalali_converter


class articlemanager(models.Manager):
    def published(self):
        return self.filter(status='p')


class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)


class Category(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL,
                               related_name='children', verbose_name="زیردسته")
    title = models.CharField(max_length=200000, verbose_name="عنوان دسته بندی")
    slug = models.SlugField(max_length=1000, unique=True, verbose_name="آدرس دسته بندی")
    status = models.BooleanField(default=True, verbose_name="نمایش بدم یا نه؟")
    position = models.IntegerField(verbose_name="پوزیشن")

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
        ordering = ['parent__id', 'position']

    def __str__(self):
        return self.title

    objects = CategoryManager()


class IpAddress(models.Model):
    ipaddress = models.GenericIPAddressField(verbose_name="آدرس ای پی")


class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'پیش نویس'),
        ('p', 'منتشر شده'),
        ('i', 'درحال بررسی'),
        ('b', 'برگشت داده شده'),
    )
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='articles',
                               verbose_name="نویسنده")
    title = models.CharField(max_length=200000, verbose_name="عنوان مقاله")
    slug = models.SlugField(max_length=1000, unique=True, verbose_name="آدرس مقاله")
    category = models.ManyToManyField(Category, verbose_name="دسته بندی", related_name="articles")
    description = models.TextField(verbose_name="توضیحات")
    Image = models.ImageField(upload_to="image", verbose_name="عکس")
    publish = models.DateTimeField(default=timezone.now(), verbose_name="زمان انتشار")
    created = models.DateTimeField(auto_now_add=True, verbose_name="ساخته شده")
    update = models.DateTimeField(auto_now_add=True, verbose_name="بروزرسانی")
    is_special = models.BooleanField(default=False, verbose_name="مقاله ویژه")
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name="وضعیت")
    comments = GenericRelation(Comment)
    hits = models.ManyToManyField(IpAddress, through="ArticleHit", blank=True, related_name="hits",
                                  verbose_name="بازدید ها")

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
        ordering = ['-publish']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("account:home")

    def jpublish(self):
        return jalali_converter(self.publish)

    jpublish.short_description = "زمان انتشار "

    # def category_publish(self):
    #     return self.category.filter(status=True)
    def Image_tag(self):
        return format_html("<img style='border-radius: 5px;' width= 80  height= 75 src='{}'>".format(self.Image.url))

    Image_tag.short_description = "تصاویر"

    def category_to_str(self):
        return " ، ".join([category.title for category in self.category.active()])

    category_to_str.short_description = "دسته بندی"

    objects = articlemanager()

class ArticleHit(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    ip_address = models.ForeignKey(IpAddress, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="ساخته شده")
