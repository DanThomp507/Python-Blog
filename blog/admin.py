from django.contrib import admin
from blog.models import Post, Category

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'created_on','last_modified',)
    #   list_display = ('title', 'slug', 'author','updated_on', 'content', 'created_on', 'status',)
    pass

class CategoryAdmin(admin.ModelAdmin):
     list_display = ('name',)
pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)