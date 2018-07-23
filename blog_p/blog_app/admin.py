"""
customize administration interface by inheriting from admin.ModelAdmin
admin.ModelAdmin configurations:
fields\exclude
fieldsets
list_display
list_display_links
list_editable
list_filter
inlines
...
"""
from django.contrib import admin
from blog_app.models import *

# display certain fields
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

# kindeditor configuration
	class Media:
		js = (
			'/static/js/kindeditor/kindeditor-all.js',
			'/static/js/kindeditor/kindeditor-all-min.js',
			'/static/js/kindeditor/zh-CN.js',
			'/static/js/kindeditor/config.js',
		)



# Register your models here.
admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Category)
# register customized model objects
admin.site.register(Article, ArticleAdmin)
# admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Links)
admin.site.register(Ad)
