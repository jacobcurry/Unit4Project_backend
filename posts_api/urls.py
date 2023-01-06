from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('api/posts', views.PostList.as_view(), name="post_list"),
    path('api/posts/profile', views.ProfilePostList.as_view(), name="profile_post_list"),
    path('api/posts/<int:pk>', views.PostDetail.as_view(), name="post_detail"),
    path('api/users', views.UserList.as_view(), name='user_list'),
    path('api/users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('api/useraccount/login', csrf_exempt(views.check_login), name="check_login")
]
