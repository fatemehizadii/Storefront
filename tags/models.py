from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
class Tag(models.Model):
    label = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.label


class TaggedItem(models.Model):
    # what tag applied to what object 
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    #type (product, video, anything)
    #ID
    #if we wnat to have a field like (product = ... ) we should import from store app and we dont want the tag app to depend on the other app so:
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    # we can read the actual object that a particular tag is applied to 
    content_object = GenericForeignKey()
    