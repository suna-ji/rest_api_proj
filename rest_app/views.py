from .models import Post
from .serializer import  PostSerializer
from rest_framework import viewsets

class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

#     # @action(method=['post'])
#     @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
#     # 그냥 얍을 띄우는 custom api
#     def highlight(self, request, *args, **kwargs):
#         return HttpResponse("얍")
