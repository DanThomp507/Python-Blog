from django.contrib import admin
from blog.models import Post, Category

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'created_on','last_modified',)
    pass

class CategoryAdmin(admin.ModelAdmin):
     list_display = ('name',)
pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)