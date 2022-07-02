from rest_framework import viewsets
from .models import Link
from .serizliers import LinkSerializer

# Create your views here.
class PostListApi(viewsets.generics.ListAPIView):
    queryset = Link.objects.filter()
    serializer_class = LinkSerializer

class PostCreateApi(viewsets.generics.CreateAPIView):
    queryset = Link.objects.filter()
    serializer_class = LinkSerializer

class PostDetailApi(viewsets.generics.RetrieveAPIView):
    queryset = Link.objects.filter()
    serializer_class = LinkSerializer

class PostUpdateApi(viewsets.generics.UpdateAPIView):
    queryset = Link.objects.filter()
    serializer_class = LinkSerializer

class PostDeleteApi(viewsets.generics.DestroyAPIView):
    queryset= Link.objects.filter()
    serializer_class = LinkSerializer