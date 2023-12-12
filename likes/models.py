 #this app is for tracking the objects that a user likes
 #LikedItem :
 # -what user likes what object
 # -user: ForeignKey to user (django.contrib.auth.models)

from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType 
from django.contrib.contenttypes.fields import GenericForeignKey

class LikedItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # if a user is deleted we want all the objects that the user has liked to be deleted
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
