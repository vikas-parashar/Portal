from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from .forms import TutorProfileForm, StudentProfileForm
from .models import ExUserProfile, TutorProfile, StudentProfile

# Create your views here.

def profile(request):
	if request.user.is_authenticated and not request.user.is_staff:
		loggeduser = [i.id for i in ExUserProfile.user.field.rel.to.objects.filter(username = request.user)]
		ruser =  ExUserProfile.user.field.rel.to.objects.filter(username = request.user)[0].id

		profile_data =   [i for i in ExUserProfile.objects.filter(id = ruser-1)][0].is_tutor

		if profile_data != 'Student':
			form = TutorProfileForm(request.POST or None)
		else:
			form = StudentProfileForm(request.POST or None)

		context = {
			"form": form,
			"ruser": ruser,
			"profile_data":profile_data,
		}

		if form.is_valid():
			form.cleaned_data
			a = form.save(commit = False)
			a.email = request.user.email
			a.save()
			return HttpResponseRedirect('/')

	return render(request, "profile.html", context)

def students(request):
	if request.user.is_authenticated and request.user.is_staff:
		data = StudentProfile.objects.all()
		context = {
		  "students_data": data
		}
	return render(request, "students.html", context)

def tutors(request):
	if request.user.is_authenticated and request.user.is_staff:
		data = TutorProfile.objects.all()
		context = {
		  "tutors_data": data
		}
	return render(request, "tutors.html", context)