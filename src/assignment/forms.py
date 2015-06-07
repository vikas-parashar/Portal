from django import forms
from .models import Assignment

class AssignmentForm(forms.ModelForm):
	class Meta:
		model = Assignment
		fields = ['main_sub', 'add_sub', 'deadline', 'details', 'amount']
		# self.fields['main_sub'].label = "Main Subject"

	# def clean_username(self):
	# 	email = self.cleaned_data.get('username')
	# 	return email