from django.db import models
from django.conf import settings

class TutorDetails(models.Model):
	#dropdown for subjects
	SUBJECTS_LIST = (
	        ( 'sub1', 'Subject1' ),
	        ( 'sub2', 'Subject2' ),
	        ( 'sub3','Subject3' ),
	    )

	email        = models.EmailField()
	full_name 	 = models.CharField(max_length=120)
	timestamp    = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated      = models.DateTimeField(auto_now_add=False, auto_now=True)

	main_subject = models.CharField(max_length="4", choices=SUBJECTS_LIST, default ='sub1')

	def __unicode__(self): #Python 3.3 is __str__
		return self.email