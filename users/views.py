from django.http import HttpResponse
import json
from django.http import JsonResponse

from django.shortcuts import  HttpResponse
from rest_framework.decorators import api_view, permission_classes

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from users.models import MyUser
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from rest_framework.permissions  import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework import status

# Create your views here.

def get_tokens_for_user(user):
    refresh = AccessToken.for_user(user)
    return {'refresh': str(refresh)}

# @csrf_exempt
# @api_view(('GET',))
# @renderer_classes([JSONRenderer])
# @login_required
def getToken(request):
    return HttpResponse(request.user)

@csrf_exempt
@api_view(('POST',))
@renderer_classes([JSONRenderer])
def signup(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
        firstName = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        mobile = data.get("mobile")
        password = make_password(data.get("password"))
        user = MyUser(first_name=firstName,last_name=last_name,email =email,password=password,mobile=mobile,is_active =True)
        user = user.save()
        # token = get_tokens_for_user(user)
        return JsonResponse({"msg":"data inserted successfully",'code':200},status=status.HTTP_200_OK, safe=True)
    except Exception as e:
        print(e)
        return JsonResponse({"error":e, "code":500},status=status.HTTP_500_INTERNAL_SERVER_ERROR ,safe=False)

# test@1234
# demo@1234

@csrf_exempt
@api_view(('POST',))
@renderer_classes([JSONRenderer])
def signin(request):
   
    try:
        data = json.loads(request.body)
        email = data['data']["email"]
        password = data['data']["password"]
        user = authenticate(username=email,password=password)
        print(user)
        if user is not None: 
            token = get_tokens_for_user(user)
            login(request, user)
            return JsonResponse({"msg":" login successfully", "token": token,'code':200},status=status.HTTP_200_OK, safe=True)
        else :
            return JsonResponse({"msg":"user not found",'code':401},status=status.HTTP_401_UNAUTHORIZED, safe=True)

    except Exception as e:
        print(e)
        return JsonResponse({"error":e, "code":500},status=status.HTTP_500_INTERNAL_SERVER_ERROR ,safe=False)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def User_logout(request):
    logout(request)
    return HttpResponse('User Logged out successfully')