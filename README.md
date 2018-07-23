1. Create virtual environment by 'virtualenv', 'pip install django==x.y.z(PILLOW, PyMySQL)';
2. 'django-admin startproject(startapp) {Filename}';
3. Add static/, templates/;
4. Add code to init.py in project root
```
import pymysql
pymysql.install_as_MySQLdb()
```
;
5. Modify settings.py, add app name, templates path, db coniguration for mysql, static path, and 'LOGGING',      
sometimes you may want to add some constnat variables for additional info;
6. Add ORM to models.py(we can inherit class from AbstractUser for customized User model)
```
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
	...
```
;
7. Execute pthon manage.py makemigrations and python manage.py createsuperuser then migrate;
8. Add routine to urls.py either project root or app;
9. Modify html file and add django tag to it with {% %},  {{}}, ...
10. Since have defined inherited User model we need to add additional info for settings then we can eliminate the conflicts.
```
# define user model
AUTH_USER_MODEL = 'blog_app.User'
```
;
11.  customize administration interface by inheriting from admin.ModelAdmin
admin.ModelAdmin configurations:
fields\eclude
fieldsets
list\_display
list\_display\_links
list\_editable
list\_filter
inlines
```
from django.contrib import admin
from blog_app.models import *

class ArticleAdmin(admin.ModelAdmin):
	fieldsets = (
		('Common features => ', {
				'fields': ('title', 'desc', 'content', )
		}),
		('Advanced features =>', {
			'classes': ('collapse',),
			'fields': ('click_count', 'is_recommend',  'user',)
		}),
	)

# display specified columns
	list_display = ('title', 'desc', 'click_count',)
	list_display_links = ('title', 'desc', 'click_count',)

```
12. add Media class to customized model in admin.py, here we use kindeditor for 
largeTextEditor use, it can be downloaded from "http://kindeditor.net/demo.php" 
```
	class Media:
		js = (
			'/static/js/kindeditor/kindeditor-all.js',
			'/static/js/kindeditor/kindeditor-all-min.js',
			'/static/js/kindeditor/zh-CN.js',
			'/static/js/kindeditor/config.js',
		)

```
We also need to create a config.js at the root path of our project and add following code
```
KindEditor.ready(function (K) {
		window.editor = K.create('textarea[name=content]',{
			width: 500,
			height: 200,
			});
		});
```

13. Register models,including the customized model
14. Don't forget to modify the views .py in app root path and add following code
```
import logging

from django.conf import settings
logger = logging.gettingLogger('blog_app.views')

# global setting
def global_setting(request):
	return {'SITE_NAME': settings.SITE_NAME, 'SITE_DESC': settings.SITE_DESC, }
```
;
