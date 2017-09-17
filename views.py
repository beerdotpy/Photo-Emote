from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from models import User, Image, Like
from django.core.files import File
from serializers import ImageSerializer, UserSerializer
from rest_framework.renderers import JSONRenderer
import json

#prod_URL = ""
debug_URL = "http://localhost:8000/"

@csrf_exempt
def createUser(request):
    data = json.loads(request.body)
    user_device_id = data["device_id"]
    try:
        user = User.objects.get(device_id = user_device_id)
    except:
        user = User.objects.create(device_id = user_device_id)
    userSerializer = JSONRenderer().render((UserSerializer(user)).data)
    return HttpResponse(userSerializer)

@csrf_exempt
def createImage(request):
    data = request.POST
    try:
        user = User.objects.get(user_id = data['user_id'])
    except:
        return HttpResponse(status = 404)

    image = Image.objects.create(user_id = user, url = request.FILES['file'], description = data['description'],\
                hashtags = data['hashtags'], orientation = data['orientation'])
    return HttpResponse(image)
    
@csrf_exempt
def imageFeed(request):
    data = json.loads(request.body)
    images = Image.objects.filter(orientation = data["orientation"])
    imageList = []
    for image in images:
        data = ImageSerializer(image).data
        data['likes_count'] = image.likes.all().count() 
        try:
            user = User.objects.get(user_id = data['user'])
            image.likes.get(user_id = user)
            data['liked_by_user'] = True
        except:
            data['liked_by_user'] = False

        imageList.append(data) 
    return HttpResponse(JSONRenderer().render(imageList), content_type="application/json")

@csrf_exempt
def onLikeImage(request):
    data = json.loads(request.body)
    try:
        user = User.objects.get(user_id = data['user_id'])
    except:
        return HttpResponse(status=404)
    try:
        image = Image.objects.get(image_id = data['image_id'])
    except:
        return HttpResponse(status=404)
    if data['action'] == 'like':
        like = Like.objects.create(like_type = data['like_type'], user_id = user, image_id = image, 
                        pixels = data['pixels'])
        return HttpResponse(status=200)
    elif data['action'] == 'dislike':
        try:
            like = Like.objects.get(user_id = user, image_id = image)
        except:
            return HttpResponse(status=404)
        like.delete()
        return HttpResponse(status=200)

