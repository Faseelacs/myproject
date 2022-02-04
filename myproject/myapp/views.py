from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import Topic,Comment,Topicandcomment
from .serializer import TopicSerializer,CommentSerializer,TopicandcommentSerializer
class TopicViewSet(ModelViewSet):
    serializer_class=TopicSerializer
    queryset=Topic.objects.all()
class CommentViewSet(ModelViewSet):
    serializer_class=CommentSerializer
    queryset=Comment.objects.all()
class TopicandcommentViewSet(ModelViewSet):
    queryset=Topicandcomment.objects.all()
    serializer_class=TopicandcommentSerializer

