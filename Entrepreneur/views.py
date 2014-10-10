# Create your views here.
from django.shortcuts import render, render_to_response
from Entrepreneur.models import *
import json
from django.utils.safestring import SafeString
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

@csrf_exempt
def create_comment(request):
    post_id = request.POST['post_id']
    comment_id = None
    comment_text = request.POST['comment_text']
    reader_id = request.POST['reader_id']
    reader_name = request.POST['reader_name']
    network = request.POST['network']
    if request.POST['image'] is not None:
        reader_image = request.POST['image']

    post = Post.objects.get(pk=post_id)
    if network=='facebook':
        reader,created = FacebookReader.objects.get_or_create(facebook_id=reader_id, name=reader_name, picture_url=reader_image)
    elif network=='twitter':
        reader,created = TwitterReader.objects.get_or_create(twitter_id=reader_id, name=reader_name, picture_url=reader_image)
    else:
        reader,created = GooglePlusReader.objects.get_or_create(google_id=reader_id, name=reader_name, picture_url=reader_image)
    if comment_id is None:
        comment = Comment(post=post, reader=reader, text=comment_text)
        comment.save()
    #else:
    #    original_comment = Comment.objects.get(pk=comment_id)
    #    comment = ResponseComment(post=post, reader=reader, text=comment_text, original_comment=original_comment)
    #    comment.save()
    serialized_comment = {}
    serialized_comment['comment_id'] = comment.comment_id
    serialized_comment['name'] = comment.reader.name
    serialized_comment['picture'] = comment.reader.picture_url
    serialized_comment['text'] = comment.text
    serialized_comment['date'] = {}
    serialized_comment['date']['day'] = comment.date.day
    serialized_comment['date']['month'] = comment.date.strftime("%B")
    serialized_comment['date']['year'] = comment.date.year
    return HttpResponse(json.dumps(serialized_comment), content_type="application/json")


def add_share(request):
    post_id = request.POST['post_id']
    post = Post.objects.get(pk=post_id)
    post.shares = post.shares+1
    post.save()


def full_post_info(post, response):
    response['date'] = {}
    response['post_id'] = post.post_id
    response['title'] = post.title
    response['text'] = post.body
    response['url'] = '/post/'+post.url
    response['shares'] = post.shares
    response['date']['day'] = post.date.day
    response['date']['month'] = post.date.strftime("%B")
    response['date']['year'] = post.date.year
    response['comment_count'] = len(post.comments_on_post.all())
    response['comments'] = []
    comments = post.comments_on_post.all()
    for comment in comments:
        comment_obj = {}
        comment_obj['date'] = {}
        comment_obj['name'] = comment.reader.name
        comment_obj['picture'] = comment.reader.picture_url
        comment_obj['text'] = comment.text
        comment_obj['comment_id'] = comment.comment_id
        comment_obj['date']['day'] = comment.date.day
        comment_obj['date']['month'] = comment.date.strftime("%B")
        comment_obj['date']['year'] = comment.date.year
        response['comments'].append(comment_obj)
    return


def short_post_info(post, response):
    response['date'] = {}
    response['post_id'] = post.post_id
    response['title'] = post.title
    response['url'] = '/post/'+post.url
    response['text'] = post.body[:1000] + '...'
    response['shares'] = post.shares
    response['comment_count'] = len(post.comments_on_post.all())
    response['date']['day'] = post.date.day
    response['date']['month'] = post.date.strftime("%B")
    response['date']['year'] = post.date.year
    return


def render_post(request, post_url):
    post = Post.objects.get(url = post_url)
    post_obj = {}
    full_post_info(post=post, response=post_obj)
    #post_obj = json.dumps(post_obj)
    return render_to_response('post.html', {'post_obj':SafeString(post_obj)})


def render_homepage(request):
    posts = Post.objects.order_by('-date')[:30]
    response = []
    for post in posts:
        post_obj = {}
        short_post_info(post, post_obj)
        response.append(post_obj)
    return render(request, 'index.html', {'post_objs': SafeString(response)}, content_type='text/html')


