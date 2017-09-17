from django.db import models
import random
import string
import datetime

class User(models.Model):
    device_id = models.CharField(max_length=255)
    user_id = models.CharField(max_length=10, editable=False)
    created_at = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.user_id = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
            self.created_at = datetime.datetime.today()
        return super(User,self).save(*args,**kwargs)
    
    def __unicode__(self):
        return self.user_id

class Image(models.Model):
    image_id = models.CharField(max_length=10, editable=False)
    url = models.ImageField(upload_to='static/images')
    user_id = models.ForeignKey(User)
    created_at = models.DateTimeField(editable=False)
    description = models.TextField()
    hashtags = models.TextField()
    orientation = models.CharField(max_length=100)

    def __unicode__(self):
        return self.image_id
     
    def save(self, *args, **kwargs):
        if not self.id:
            self.image_id = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
            self.created_at = datetime.datetime.today()
        return super(Image, self).save(*args, **kwargs)

    @property
    def user(self):
        return self.user_id.user_id

class Like(models.Model):
    like_type = models.CharField(max_length=20, default="Like")
    user_id = models.ForeignKey(User)
    image_id = models.ForeignKey(Image, related_name='likes')
    pixels = models.CharField(max_length=50)
    created_at = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = datetime.datetime.today()
        return super(Like, self).save(*args, **kwargs)

