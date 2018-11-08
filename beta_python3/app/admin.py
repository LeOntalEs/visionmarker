from django.contrib import admin
from .models import MyUser, Batch, Image, Label, Comment

class MyUserAdmin(admin.ModelAdmin):
	list_display=('user','isreviewer')
	list_filter=('isreviewer',)
	list_editable =('isreviewer',)

class BatchAdmin(admin.ModelAdmin):
	list_display=('id','status','reviewer', 'labeller','num_rework','created_time',
		'updated_time')
	list_filter=('status','labeller','reviewer')
	list_editable =('labeller',)
	

class ImageAdmin(admin.ModelAdmin):
	list_display=('batch','src_path','raw_path')

class LabelAdmin(admin.ModelAdmin):
	list_display=('image','x','y','width',
		'height','brand','model','color','nickname',)
	list_filter=('brand','model','color','nickname',)

class CommentAdmin(admin.ModelAdmin):
	list_display=('user', 'created_time', 'message', 'batch')
	list_filter=('user', 'batch') 

admin.site.register( MyUser, MyUserAdmin)
admin.site.register( Batch, BatchAdmin)
admin.site.register( Image, ImageAdmin)
admin.site.register( Label, LabelAdmin)
admin.site.register( Comment, CommentAdmin)
