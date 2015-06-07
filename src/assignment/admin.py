from django.contrib import admin

# Register your models here.
from .forms import AssignmentForm
from .models import Assignment

class AssignmentAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "main_sub", "add_sub", "deadline", "details", "amount", "timestamp"]
	list_filter = ('main_sub', 'add_sub')
	form = AssignmentForm
	# class Meta:
	# 	model = Assignment



admin.site.register(Assignment, AssignmentAdmin)