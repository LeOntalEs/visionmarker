from __future__ import unicode_literals
from django.conf import settings
from django.db import models

TODO='1'
TAGGING='2'
REVIEWING='3'
DONE='4'
STATUS_CHOICES = (
	(TODO, 'To do'),
    (TAGGING, 'To be labelled'),
    (REVIEWING, 'To be reviewed'),
    (DONE, 'Done')
)

class MyUser(models.Model):
	user = models.ForeignKey( settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
	isreviewer = models.BooleanField(default=False)
	def __unicode__(self):
		return self.user.username

class Batch(models.Model):
	reviewer = models.ForeignKey( 'MyUser' ,related_name='reviewer', on_delete=models.CASCADE, null=True)
	labeller = models.ForeignKey( 'MyUser' ,related_name='labeller', on_delete=models.CASCADE, null=True)
	created_time = models.DateTimeField(auto_now_add=True)
	updated_time = models.DateTimeField(auto_now=True)
	status = models.CharField( max_length=1, choices=STATUS_CHOICES, default=TODO)
	num_rework = models.PositiveSmallIntegerField(default=0)
	def __unicode__(self):
		if self.id:
			return "BID%06d"%self.id
		else:
			return "BID..."

class Comment(models.Model):
	user=models.ForeignKey( 'MyUser' , on_delete=models.CASCADE,blank=True)
	created_time = models.DateTimeField(auto_now_add=True)
	message=models.CharField(max_length=20)
	batch=models.ForeignKey( 'Batch' , on_delete=models.CASCADE,blank=True)


class Image(models.Model):
	batch = models.ForeignKey( 'Batch' , on_delete=models.CASCADE)
	src_path = models.CharField( max_length=50)
	raw_path = models.CharField( max_length=20)
	def __unicode__(self):
		return self.src_path

class Label(models.Model):
	image = models.ForeignKey( 'Image' , on_delete=models.CASCADE)
	x = models.PositiveSmallIntegerField(blank=False)
	y = models.PositiveSmallIntegerField(blank=False)
	width = models.PositiveSmallIntegerField(blank=False)
	height = models.PositiveSmallIntegerField(blank=False)
	brand = models.CharField(max_length=20)
	model = models.CharField(max_length=20)
	color = models.CharField(max_length=10)
	nickname = models.CharField(max_length=20,blank=True)
	def __unicode__(self):
		return "LID%07d"%self.id

