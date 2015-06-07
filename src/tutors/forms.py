from django import forms

from .models import TutorDetails

class TutorDetailsForm(forms.ModelForm):
	class Meta:
		model = TutorDetails
		fields = ['full_name', 'email', 'main_subject']
	def clean_email(self):
		email = self.cleaned_data.get('email')
		return email