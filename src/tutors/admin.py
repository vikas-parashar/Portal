from django.contrib import admin

# Register your models here.
from .forms import TutorDetailsForm
from .models import TutorDetails

class TutorDetailsAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "full_name", "main_subject", "timestamp"]
	form = TutorDetailsForm
	# class Meta:
	# 	model = TutorDetails



admin.site.register(TutorDetails, TutorDetailsAdmin)