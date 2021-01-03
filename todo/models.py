from django.db import models


# Create your models here.
class Item(models.Model):
    # null=False prevents items from being created without a
    # name programmatically
    # blank=False will make the field required on forms
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    # self is the class itself as its own arguement
    # It will return self.name which is the class's name attribute
    def __str__(self):
        return self.name
