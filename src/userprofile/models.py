from django.db import models
from django.core.validators import RegexValidator
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
# make query like this a = ExUserProfile.user.field.rel.to.objects.all() for thiss model
class ExUserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    is_tutor = models.CharField(max_length="10", default=False)

    def __unicode__(self):
        return unicode(self.user)


from registration.signals import user_registered

def user_registered_callback(sender, user, request, **kwargs):
    profile = ExUserProfile(user = user)
    profile.is_tutor = request.POST['is_tutor']
    profile.save()

user_registered.connect(user_registered_callback)

class TutorProfile(models.Model):
	#dropdown for subjects
	SUBJECTS_LIST = (
	        ( 'sub1', 'Subject1' ),
	        ( 'sub2', 'Subject2' ),
	        ( 'sub3', 'Subject3' ),
	    )

	full_name	 = models.CharField(max_length="60")
	phone_regex  = RegexValidator(regex=r'^[789]\d{9}$', message="Phone number must be entered in the format: '999999999'.")
	phone_no 	 = models.CharField(max_length=10, validators=[phone_regex])
	subject = models.CharField(max_length="4", choices=SUBJECTS_LIST, default ='sub1')
	timestamp    = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated      = models.DateTimeField(auto_now_add=False, auto_now=True)
	email    = models.EmailField(blank=True)

	def __unicode__(self):
		return self.full_name

class StudentProfile(models.Model):
	full_name	 = models.CharField(max_length="60")
	phone_regex  = RegexValidator(regex=r'^[789]\d{9}$', message="Phone number must be entered in the format: '999999999'.")
	phone_no 	 = models.CharField(max_length=10, validators=[phone_regex])
	timestamp    = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated      = models.DateTimeField(auto_now_add=False, auto_now=True)
	email    = models.EmailField()

	def __unicode__(self):
		return self.full_name
