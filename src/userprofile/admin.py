from django.contrib import admin
from .forms import ExUserProfileForm, StudentProfileForm, TutorProfileForm
from .models import ExUserProfile, StudentProfile, TutorProfile

class ExUserProfileAdmin(admin.ModelAdmin):
    class Meta:
    	list_display = ['user', 'is_tutor']
    	form = ExUserProfileForm

    class Meta:
      form = StudentProfileForm
      list_display = ['full_name', 'phone_no', 'timestamp']

    class Meta:
      form = TutorProfileForm
      list_display = ['full_name', 'phone_no', 'timestamp']


admin.site.register(ExUserProfile, ExUserProfileAdmin)
admin.site.register(StudentProfile, ExUserProfileAdmin)
admin.site.register(TutorProfile, ExUserProfileAdmin)