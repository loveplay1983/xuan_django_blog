from django.shortcuts import render
import logging
from django.conf import settings

logger = logging.getLogger('blog_app.views')


# global setting
def global_setting(request):
	return {'SITE_NAME': settings.SITE_NAME, 'SITE_DESC': settings.SITE_DESC, }


def index(request):
	try:
		file = open('test.txt', 'r')
	except Exception as e:
		logger.error(e)
	return render(request, 'index.html', locals())
