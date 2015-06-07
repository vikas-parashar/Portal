
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail, BadHeaderError, send_mass_mail
from django.shortcuts import get_object_or_404
from django.template.loader import get_template, render_to_string
from django.conf import settings

from tutors.models import TutorDetails

# from .forms import TutorProfileForm, StudentProfileForm
from userprofile.models import ExUserProfile, TutorProfile, StudentProfile

from .models import Assignment
from .forms import AssignmentForm

def home(request):
	title   = "Studyportal"
	context = { "title" : title }


	#FOR ADMIN ACCOUNT
	if request.user.is_authenticated and request.user.is_staff:

		assign_details = Assignment.objects.all()


		context = {
			"assign_details": assign_details
		}
	#FOR USER ACCOUNTS
	if request.user.is_authenticated and not request.user.is_staff:
		# tutor_details = TutorDetails.objects.all()
		try:
			logged_user_list = [i.id for i in ExUserProfile.user.field.rel.to.objects.filter(username = request.user)]
			logged_user_id   =  ExUserProfile.user.field.rel.to.objects.filter(username = request.user)[0].id
			logged_user_name = [i for i in ExUserProfile.objects.filter(id = logged_user_id-1)][0]

			profile_data     =   logged_user_name.is_tutor
			logged_user      = request.user
			logged_user_mail = logged_user.email

			if profile_data != 'Tutor':
				assign_details = Assignment.objects.filter(username = logged_user)
			else:
				# a = ExUserProfile.user.field.rel.to.objects.filter(username = request.user)
				tutor_details = get_object_or_404(TutorProfile, email = logged_user_mail)
				assign_details = Assignment.objects.filter(main_sub = tutor_details.subject)

			context = {
				"profile_data": profile_data,
				"assign_details": assign_details,
				"logged_user":	  logged_user

			}
		except IndexError:
			print IndexError

	return render(request, "home.html", context)



def assignment_form(request):

	form = AssignmentForm(request.POST or None)
	context = {
		"form": form,
	}
	if form.is_valid():
		Assignment1 = form.save(commit=False)
		Assignment1.username = request.user
		Assignment1.save()

		return HttpResponseRedirect("/")
	return render(request, "form.html", context)


def assignment_details(request, user_id):
	if request.user.is_authenticated and request.user.is_staff:
		assign_details = get_object_or_404(Assignment, pk = user_id)

		tutor_details  = TutorProfile.objects.filter(subject = assign_details.main_sub)
		# print "test"
		context = {
			"assign_details": assign_details,
			"tutor_details" : tutor_details,
		}

		email_template_html = "assign-details-table.html"
		email_template_txt  = "assign-details-table.txt"
		mail_list           = [el.email for el in tutor_details]
		from_email 			= settings.DEFAULT_FROM_EMAIL
		subject    			= "Assignment for you"
		text_content  		= render_to_string(email_template_txt, context)
		html_content    	= render_to_string(email_template_html, context)

		if subject and text_content and from_email :
			try:
				# sendmail = EmailMessage(subject, message, to=['svnitvikas@gmail.com'])
				# sendmail.send(fail_silently=False)
				send_mail(subject, text_content, from_email, mail_list, fail_silently=False, html_message=html_content)
				print "mail sent"
			except BadHeaderError:
				return HttpResponse('Invalid header found.')

		return render(request, "assign-details.html", context)



def mail(request):
	if request.user.is_authenticated and request.user.is_staff:
		email_template = "assign-details-table.html"
		print "test 2"

		from_email = "svnitvikas@gmail.com"
		subject    = "Assignment for you"
		message    = "get_template(email_template)"
		if subject and message and from_email :
			try:
				sendmail = EmailMessage(subject, message, to=['svnitvikas@gmail.com'])
				sendmail.send(fail_silently=False)
				# send_mail(topic, message, from_email, ['svnitvikas@gmail.com'], EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return HttpResponse()

	return HttpResponseRedirect("/thankyou/")