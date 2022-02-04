from rest_framework.routers import DefaultRouter
from .views import TopicViewSet,CommentViewSet,TopicandcommentViewSet
from django.urls import path,include
router=DefaultRouter()
router.register('topic',TopicViewSet)
router.register('comment',CommentViewSet)
router.register('topicandcomment',TopicandcommentViewSet)

urlpatterns= [
    path('',include(router.urls))
    ]
