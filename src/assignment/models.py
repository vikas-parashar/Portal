from django.db import models
# from django.forms.widgets import *
# Create your models here.

class Assignment(models.Model):
	#dropdown for subjects
	SUBJECTS_LIST = (
	        ( 'sub1', 'Subject1' ),
	        ( 'sub2', 'Subject2' ),
	        ( 'sub3','Subject3' ),
	    )

	#DROPDOWN FOR DUE_TIME
	DUE_TIME_LIST = (
	        ( '12 hours', '12 hours' ),
	        ( '24 hours', '24 hours' ),
	        ( '2 days','2 days' ),
	        ( '3 days','3 days' ),
	        ( '4 days','4 days' ),
	        ( '5 days','5 days' ),
	        ( '6 days','6 days' ),
	        ( '1 week','1 week' ),
	        ( 'More than 1 week','More than 1 week' ),
	    )

	main_sub	 = models.CharField("Main Subject", max_length="60", choices=SUBJECTS_LIST, default ='sub1')
	add_sub 	 = models.CharField("Additional Subject", max_length="60", choices=SUBJECTS_LIST, default ='sub1')
	deadline	 = models.CharField("Deadline", max_length="60", choices=DUE_TIME_LIST, default ='12 hours')
	details		 = models.TextField()
	timestamp	 = models.DateTimeField(auto_now_add=True, auto_now=False)
	username	 = models.CharField(max_length="60")
	amount		 = models.IntegerField()

	def __unicode__(self):
		return self.username