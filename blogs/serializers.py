from rest_framework import serializers
from blogs.models import blogs,blog_category

class BlogSerializer(serializers.ModelSerializer):                                                                                                                                                                                                                                  
    class Meta:                                                                                                                                                                                                   
        model = blogs                                                                                                                                                                                         
        fields = ('id', 'title','category','file','content', 'summary','author','referel_link','createdAt', 'created_by')


class CategorySerializer(serializers.ModelSerializer):                                                                                                                                                                                                                                  
    class Meta:                                                                                                                                                                                                   
        model = blog_category                                                                                                                                                                                         
        fields = ('id', 'category_name', 'createdAt')
        