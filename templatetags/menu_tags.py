from django import template
from menu.models import *

register = template.Library()


@register.inclusion_tag('menu/tags/menu.html')
def menu(menu_name):
    return {
        'menu_items': Menu.objects.get(menu_name=menu_name).items,
    }
