from django import forms
from .models import TutorProfile, StudentProfile
from django.utils.safestring import mark_safe



class HorizontalRadioRenderer(forms.RadioSelect.renderer):
    """ this overrides widget method to put radio buttons horizontally
        instead of vertically.
    """
    def render(self):
            """Outputs radios"""
            return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

from registration.forms import RegistrationForm
from django import forms

class ExUserProfileForm(RegistrationForm):
	CHOICES = (
		('Student','Student'),
		('Tutor','Tutor')
		)
	is_tutor =  forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(renderer=HorizontalRadioRenderer))

class TutorProfileForm(forms.ModelForm):

	class Meta:
		model 	= TutorProfile
		fields  = ['full_name', 'phone_no', 'subject']

class StudentProfileForm(forms.ModelForm):

	class Meta:
		model 	= StudentProfile
		fields  = ['full_name', 'phone_no']