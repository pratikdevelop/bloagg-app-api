from django.contrib import admin
from blogs.models import blogs,blog_category

# Now register the new UserAdmin...
@admin.register(blogs)
class Blogs(admin.ModelAdmin):
    list_display = ('id', 'title','author', 'category', 'file', 'createdAt')
    search_fields = ('title','category')
    ordering = ('title',"id", 'category', 'createdAt')


@admin.register(blog_category)
class Blogscategory(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'createdAt')