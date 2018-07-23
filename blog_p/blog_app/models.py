from django.db import models
from django.contrib.auth.models import AbstractUser


# define db models
# type1 => inheriting from AbstractUser
# type2 => defining db models base on relational objects(OneToOne, OneToMany, ManyToMany...)

# USER
class User(AbstractUser):
	avatar = models.ImageField(upload_to='avatar/%Y/%m', default='avatar/default.png', max_length=200, blank=True, null=True, verbose_name='Avatar')
	qq = models.CharField(max_length=20, blank=True, null=True, verbose_name='QQ')
	mobile = models.CharField(max_length=11, blank=True, null=True, unique=True, verbose_name='Mobile')

	class Meta:
		verbose_name = 'User'
		verbose_name_plural = verbose_name
		ordering = ['-id']

	def __unicode__(self):
		return self.username


# TAG
class Tag(models.Model):
	name = models.CharField(max_length=30, verbose_name='Tag')

	class Meta:
		verbose_name = 'Tag'
		verbose_name_plural = verbose_name
		ordering = ['id']

	def __unicode__(self):
		return self.name


# CATEGORY
class Category(models.Model):
	name = models.CharField(max_length=30, verbose_name='Category')
	index = models.IntegerField('Ordering(ASC)', default=999)

	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = verbose_name
		ordering = ['index', 'id']

	def __unicode__(self):
		return self.name


# ARTICLE MODELS
class Article(models.Model):
	title = models.CharField(max_length=50, verbose_name='Article_Title')
	desc = models.CharField(max_length=50, verbose_name='Article_Description')
	content = models.TextField(verbose_name='Article_Content')
	click_count = models.IntegerField(default=0, verbose_name='Click_Count')
	is_recommend = models.BooleanField(default=False, verbose_name='Is_Recommend')
	date_publish = models.DateTimeField(auto_now_add=True, verbose_name='Date_Publish')
	user = models.ForeignKey(User, verbose_name='User')
	category = models.ForeignKey(Category, blank=True, null=True, verbose_name='Category')
	tag = models.ManyToManyField(Tag, verbose_name='Tag')

	class Meta:
		verbose_name = 'Article'
		verbose_name_plural = verbose_name
		ordering = ['-date_publish']

	def __unicode__(self):
		return self.title


# COMMENT
class Comment(models.Model):
	content = models.TextField(verbose_name='Comment_Content')
	date_publish = models.DateTimeField(auto_now_add=True, verbose_name='Date_Publish')
	user = models.ForeignKey(User, blank=True, null=True, verbose_name='User')
	article = models.ForeignKey(Article, blank=True, null=True, verbose_name='Article')
	pid = models.ForeignKey('self', blank=True, null=True, verbose_name='Parent_Comment')

	class Meta:
		verbose_name = 'Comment'
		verbose_name_plural = verbose_name
		ordering = ['-date_publish']

	def __unicode__(self):
		return str(self.id)


# LINKS
class Links(models.Model):
	title = models.CharField(max_length=50, verbose_name='Link_Title')
	description = models.CharField(max_length=200, verbose_name='Link_Description')
	callback_url = models.URLField(verbose_name='URL')
	date_publish = models.DateTimeField(auto_now_add=True, verbose_name='Date_Publish')
	index = models.IntegerField(default=999, verbose_name='Ordering(ASC)')

	class Meta:
		verbose_name = 'Friendly_Link'
		verbose_name_plural = verbose_name
		ordering = ['index', 'id']

	def __unicode__(self):
		return self.title


# ADVERTISMENT
class Ad(models.Model):
	title = models.CharField(max_length=50, verbose_name='AD_Title')
	description = models.CharField(max_length=200, verbose_name='AD_Description')
	image_url = models.ImageField(upload_to='ad/%Y/%m', verbose_name='Img_URL')
	callback_url = models.URLField(null=True, blank=True, verbose_name='Callback_URL')
	date_publish = models.DateTimeField(auto_now_add=True, verbose_name='Date_Publish')
	index = models.IntegerField(default=999, verbose_name='Ordering(ASC)')

	class Meta:
		verbose_name = u'AD'
		verbose_name_plural = verbose_name
		ordering = ['index', 'id']

	def __unicode__(self):
		return self.title
