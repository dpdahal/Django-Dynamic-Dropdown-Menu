from django.db import models


# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_children(self):
        return Menu.objects.filter(parent=self)


