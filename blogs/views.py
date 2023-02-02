import json
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rest_framework.permissions  import IsAuthenticated
from users.models import MyUser
from blogs.serializers import BlogSerializer, CategorySerializer
from blogs.models import blogs,blog_category
# Create your views here.

@api_view(('GET',))
        # 'rest_framework.permissions.IsAuthenticatedOrReadOnly'
# @permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def getBlogs(request):
    try:
        all_blogs = blogs.objects.all()
        serialize_blogs =  BlogSerializer(all_blogs, many=True)
        return JsonResponse(list(serialize_blogs.data),status=status.HTTP_200_OK ,safe=False)
    except Exception as e:
        return JsonResponse({"error_msg":e, 'code':500, status: False},status=status.HTTP_500_INTERNAL_SERVER_ERROR ,safe=False)



@api_view(('GET',))
@renderer_classes([JSONRenderer])
def getBlogsById(request, id):
    try:
        blog = blogs.objects.get(id = id)
        print(blog)
        serialixeBlog = BlogSerializer(blog) 
        # if(serialixeBlog.is_valid()):
            # print('deom')
        print(serialixeBlog.data)
        return JsonResponse((serialixeBlog.data),status=status.HTTP_200_OK ,safe=False)
    except ValueError as value:
        return JsonResponse({"error_msg": "user id must be integer"},status=status.HTTP_500_INTERNAL_SERVER_ERROR ,safe=False)
    except Exception as e:
        return JsonResponse({"error_msg":e},status=status.HTTP_500_INTERNAL_SERVER_ERROR ,safe=False)


def getAllCategories(request):
    try:
        category = blog_category.objects.all()
        serializeCategory = CategorySerializer(category,many=True)
        return JsonResponse(list(serializeCategory.data),status=status.HTTP_200_OK ,safe=False)
    except Exception as e:
        # print(e)
        return JsonResponse({"error_msg":e},status=status.HTTP_500_INTERNAL_SERVER_ERROR ,safe=False)


@csrf_exempt
@api_view(('POST',))
@renderer_classes([JSONRenderer])
def newBlog(request):
    
    title =request.POST.get('title')
    category_name =request.POST.get('category_name')
    summary =request.POST.get('summary')
    content =request.POST.get('content')
    url =request.POST.get('url')
    file =request.FILES.get('file')
    created_by  = 'admin@gmail.com'
    
    user = MyUser.objects.get(id=1)
    # return HttpResponse('demo')
    try: 
        blog = blogs(title=title, summary=summary,  content=content, referel_link=url,file=file,category=category_name, created_by=created_by ,author= user)
        blog.save()
        return JsonResponse({'success': True, 'msg': 'blog add successfully'},status=status.HTTP_200_OK ,safe=False)
    except Exception as e:
        print(e)
        return JsonResponse({"error_msg":e},status=status.HTTP_500_INTERNAL_SERVER_ERROR ,safe=False)



@csrf_exempt
@api_view(('POST',))
@renderer_classes([JSONRenderer])
def updateBlog(request, blogId):
    
    title =request.POST.get('title')
    category_name =request.POST.get('category_name')
    summary =request.POST.get('summary')
    content =request.POST.get('content')
    url =request.POST.get('url')
    created_by  = 'admin@gmail.com'
    
    user = MyUser.objects.get(id=1)
    try: 
        if(request.FILES.get('file')): 
            file = request.FILES.get('file')
            blog = blogs(title=title, summary=summary,  content=content, referel_link=url,file=file,category=category_name, created_by=created_by ,author= user, id=blogId)
        else:
            blog = blogs(title=title, summary=summary,  content=content, referel_link=url,category=category_name, created_by=created_by ,author= user, id=blogId)
        blog.save()
        return JsonResponse({'success': True, 'msg': 'blog add successfully'},status=status.HTTP_200_OK ,safe=False)
    except Exception as e:
        print(e)
        return JsonResponse({"error_msg":e},status=status.HTTP_500_INTERNAL_SERVER_ERROR ,safe=False)