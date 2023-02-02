from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.getBlogs),
    path('blog/<str:id>', views.getBlogsById),
    path('edit-blog/<str:blogId>', views.updateBlog),
    
    path('add-blog', views.newBlog),
    path('category', views.getAllCategories)
]
