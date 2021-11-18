from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView,GenericAPIView,ListCreateAPIView
from rest_framework import mixins
from . models import BlogPost,Feedback
from . serializers import BlogPostSerializer,FeedbackSerializer
from rest_framework import status

# Create your views here.

class BlogPostListView(ListAPIView):
    serializer_class = BlogPostSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = BlogPost.objects.order_by('-date_created')
    lookup_field = 'slug'
 
class BlogPostDetailView(RetrieveAPIView):
    serializer_class = BlogPostSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = BlogPost.objects.order_by('-date_created')
    lookup_field = 'slug'

class BlogPostFeaturedView(ListAPIView):
    serializer_class = BlogPostSerializer
    queryset = BlogPost.objects.all().filter(featured=True)
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny,)

class BlogPostCategoryView(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request, format=None):
        data = self.request.data
        category = data['category']
        queryset = BlogPost.objects.order_by('-date_created').filter(category__iexact=category)
        serializer = BlogPostSerializer(queryset, many= True)
        return Response(serializer.data)

    
class FeedbackView(GenericAPIView,mixins.CreateModelMixin,mixins.ListModelMixin):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    