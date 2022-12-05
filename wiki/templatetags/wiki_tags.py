from django import template

from wiki.models import Category

register = template.Library()

@register.simple_tag()
def get_categories():  
    return Category.objects.all() #будут возвращаться все категории

@register.inclusion_tag('wiki/list_categories.html')
def show_categories(arg1 = '', arg2 = ''):
    categories = Category.objects.all()
    return {'categories': categories, 'arg1' : arg1, 'arg2' : arg2}