from django.db import models
import datetime

class Reader(models.Model):
    reader_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000)
    picture_url = models.URLField(default="img/unknown_reader.jpg")

	
class FacebookReader(Reader):
    facebook_id = models.BigIntegerField(primary_key=True)

class TwitterReader(Reader):
    twitter_id = models.BigIntegerField(primary_key=True)

class GooglePlusReader(Reader):
    google_id = models.CharField(primary_key=True, max_length=50)

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, unique=True)
    body = models.TextField()
    url = models.URLField(unique=True)
    shares = models.IntegerField(default=0)
    date = models.DateField(default=datetime.datetime.now())

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, related_name="comments_on_post")
    reader = models.ForeignKey(Reader, related_name="comments_by_user")
    text = models.TextField()
    date = models.DateField(default=datetime.datetime.now())

class ResponseComment(Comment):
    original_comment = models.ForeignKey(Comment, related_name="response_comments")

