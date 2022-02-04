from django.db import models

#  Create your models here.

class Topic(models.Model):
    name=models.CharField(max_length=20)
    
class Topicandcomment(models.Model):
    topic_id=models.ForeignKey(Topic,on_delete=models.CASCADE) 
    comment=models.CharField(max_length=70)
    
   
class Comment(models.Model):
    name=models.CharField(max_length=20)
    
