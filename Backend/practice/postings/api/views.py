from rest_framework import generics
from postings.models import BlogPost 
from .serializers import BlogPostSerializer

class BlogPostRUDView(generics.ListAPIView):

    serializer_class = BlogPostSerializer
    queryset = BlogPost.objects.all()


class BlogPostDetailView(generics.RetrieveAPIView):
    serializer_class = BlogPostSerializer
    queryset = BlogPost.objects.all()