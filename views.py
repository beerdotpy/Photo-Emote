from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from models import User, Image
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
    data = json.loads(request.body)
    try:
        user = User.objects.get(user_id = data['user_id'])
    except:
        return HttpResponse(status = 404)

    image = Image.objects.create(user_id = user, url = data['image'], description = data['description'],\
                orientation = data['orientation'])
    return HttpResponse(image)
    
@csrf_exempt
def imageFeed(request):
    data = json.loads(request.body)
    images = Image.objects.filter(orientation = data["orientation"])
    imageList = JSONRenderer().render((ImageSerializer(images, many=True)).data)
    return HttpResponse(imageList, content_type="application/json")
    


