from django.contrib import admin
from .models import Article, Category
from .models import IpAddress
admin.site.site_header = "اولین تست "


def make_published(modeladmin, request, queryset):
    rows_updated = queryset.update(status='p')
    if rows_updated == 1:
        message_bit = "منتشر شد"
    else:
        message_bit = "منتشر شدند"
    modeladmin.message_user(request, "{} مقاله {}" .format(rows_updated, message_bit))
make_published.short_description = "انتشار مقالات انتخاب شده"

def make_draft(modeladmin, request, queryset):
    rows_updated = queryset.update(status='d')
    if rows_updated == 1:
        message_bit = "پیش نویس شد"
    else:
        message_bit = "پیش نویس شدند"
    modeladmin.message_user(request, "{} مقاله {}".format(rows_updated, message_bit))

make_draft.short_description = "پیش نویس کردن مقالات"

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'Image_tag', 'slug', 'jpublish', 'is_special','status', 'category_to_str', 'author')
    list_filter = ('title', 'slug', 'author')
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['status']
    actions = [make_published, make_draft]




admin.site.register(Article, ArticleAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'slug', 'title', 'status', 'parent')
    list_filter = (['status'])
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(IpAddress)