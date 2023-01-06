from django.shortcuts import render
from rest_framework import generics, filters
from .serializers import PostSerializer, UserSerializer
from .models import Post, User
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
import json
# Create your views here.

class PostList(generics.ListCreateAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    queryset = Post.objects.all().order_by('-id')
    serializer_class = PostSerializer

class ProfilePostList(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = Post.objects.all().order_by('-id')
        userid = self.request.query_params.get('userid')
        if userid is not None:
            queryset = queryset.filter(user_id = userid)
        return queryset




        
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all().order_by('-id')
    serializer_class = PostSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = UserSerializer # tell django what serializer to use

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

def check_login(request):
    if request.method=='Get':
        return JsonResponse({})

    if request.method=='PUT':
        JsonRequest = json.loads(request.body)
        email = JsonRequest['email']
        password = JsonRequest['password']
        try :
            user = User.objects.get(email=email)
            if check_password(password, user.password):
                return JsonResponse({'id': user.id, 'firstname': user.firstname, 'lastname': user.lastname, 'username':user.username, 'email': user.email})
            else:
                return JsonResponse({'password' : 'Incorrect password'}, status=500)
        except:
            return JsonResponse({'email' : 'Email does not exist'}, status=500)