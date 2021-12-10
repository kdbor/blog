from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView,GenericAPIView,ListCreateAPIView
from rest_framework import mixins
from . models import BlogPost,Feedback
from . serializers import BlogPostSerializer,FeedbackSerializer,DataSerializer
from rest_framework import status

from .tests import Data

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

# Data view to be rendered on plotly

@api_view(['GET','POST'])
def data_view(request):
    
    # xcors = ' '.join(map(str, [2,4,6,8,10,12,14,16,18,20]))
    # ycors = ' '.join(map(str, [4,16,36,64,100,144,196,256,324,400]))
    # print(xcors)
    # print(ycors)
    data = Data(xcors = [2,4,6,8,10,12,14,16,18,20], ycors = [4,16,36,64,100,144,196,256,324,400])
    serializer = DataSerializer(data)
    return Response(serializer.data)
    
    