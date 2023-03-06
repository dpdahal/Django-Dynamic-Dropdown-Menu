from .models import *


def menu_data(request):
    data = {
        'menuData': Menu.objects.filter(parent=None)
    }
    return data
