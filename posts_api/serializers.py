from rest_framework import serializers
from .models import Post, User

from django.contrib.auth.hashers import make_password

class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = ('id', 'user_id', 'username', 'title', 'formBody', 'imageURL', 'likes', 'upvoted','downvoted', 'created')

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'firstname', 'lastname', 'email', 'username', 'password')

  def create(self, validated_data):
    user = User.objects.create(
    firstname=validated_data['firstname'],
    lastname=validated_data['lastname'],
    email=validated_data['email'],
    username=validated_data['username'],
    password= make_password(validated_data['password'])
    )
    user.save()
    print(user)
    return user

  def update(self, instance, validated_data):
    user = User.objects.get(email=validated_data["email"])
    user.password = make_password(validated_data["password"])
    user.save()
    return user



# class PostSerializer(PostSerializerBase):
#   user = UserSerializer(many=True)
#   class Meta(PostSerializerBase.Meta):
#     fields = PostSerializerBase.Meta.fields
