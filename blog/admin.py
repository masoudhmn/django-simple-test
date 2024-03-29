from django.contrib import admin,messages
from .models import Article,Category
from django.utils.translation import ngettext


#admin header change
admin.site.site_header = "وبلاگ"

#admin.site.disable_action('delete_selected')

# Register your models here.
# action in admin
def make_published(modeladmin,request,queryset):
    updated = queryset.update(status='p')
    modeladmin.message_user(request, ngettext(
        '%d مقاله منتشر شد',
        '%d مقاله منتشر شدند',
        updated,
    ) % updated, messages.SUCCESS)
make_published.short_description = "انتشار مقالات انتخاب شده"

def make_draft(modeladmin,request,queryset):
    updated = queryset.update(status='d')
    modeladmin.message_user(request, ngettext(
        '%d مقاله پیش‌نویس شد',
        '%d مقاله پیش‌نویس شدند',
        updated,
    ) % updated, messages.SUCCESS)
make_draft.short_description = "پیش‌نویس شدن مقالات انتخاب شده"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position',"title" ,"slug","parent" ,"status")
    list_filter = (['status'])
    search_fields = ('title','slug')
    prepopulated_fields = {'slug':('title',)}
    
admin.site.register(Category, CategoryAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title","thumbnail_tag" ,"slug" ,'author', "jpublish" ,'is_special',"status",'category_to_str')
    list_filter = ('publish', 'status','author')
    search_fields = ('title','description')
    prepopulated_fields = {'slug':('title',)}
    ordering = ['-status','publish']
    actions = [make_published,make_draft]

    

admin.site.register(Article, ArticleAdmin)