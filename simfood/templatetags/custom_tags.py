# custom_tags.py
from django import template
from ..models import Allmenu,Category

register = template.Library()

@register.simple_tag
def show_allmenu():
	count = Allmenu.objects.count()
	return count

@register.inclusion_tag('simfood/allcategory.html')
def all_category():
	cats = Category.objects.all()
	return {'allcats': cats}
