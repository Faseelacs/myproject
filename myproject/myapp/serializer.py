from rest_framework.serializers import ModelSerializer
from .models import Topic,Comment,Topicandcomment
class TopicSerializer(ModelSerializer):
    class Meta :
        model=Topic
        fields='__all__'
class CommentSerializer(ModelSerializer):
    class Meta :
        model=Comment
        fields='__all__'

class TopicandcommentSerializer(ModelSerializer):
    class Meta :
        model= Topicandcomment
        fields=['id','topic_id','comment']
