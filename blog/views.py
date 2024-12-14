from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from blog.models import Post
from blog.serializers import PostSerializer

# Create your views here.

class BlogListView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request, *args, **kwargs):
        posts = Post.postsobjects.all()
        serializer = PostSerializer(posts, many=True)
        
        return Response(serializer.data)

class PostDetailView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request, slug, *args, **kwargs):
        post =  get_object_or_404(Post, slug=slug)
        serializer = PostSerializer(post)
        
        return Response(serializer.data)