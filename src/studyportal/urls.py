from django.conf.urls import include, url
from django.contrib import admin


#MY IMPORTS
from django.conf import settings
from django.conf.urls.static import static
from userprofile.forms import ExUserProfileForm
from registration.backends.default.views import RegistrationView
from registration.forms import RegistrationFormUniqueEmail, RegistrationFormTermsOfService

urlpatterns = [
	url(r'^$', 'assignment.views.home', name="home"),
    url(r'^profile/', 'userprofile.views.profile', name="profile"),
    url(r'^tutor/', 'tutors.views.tutor', name="tutor"),
    url(r'^form/', 'assignment.views.assignment_form', name="form"),
    url(r'^[a-z0-9_\-@+.]{0,30}/(?P<user_id>[0-9]{1,5})/', 'assignment.views.assignment_details',),

    url(r'^students/', 'userprofile.views.students', name="students"),
    url(r'^tutors/', 'userprofile.views.tutors', name="tutors"),

    url(r'^admin/', include(admin.site.urls)),
    url(r'accounts/register/$',
        RegistrationView.as_view(form_class = ExUserProfileForm),
        name = 'registration_register'),
    # url(r'accounts/register/$',
    #     RegistrationView.as_view(form_class = RegistrationFormTermsOfService),
    #     name = 'registration_register'),
    url(r'^accounts/', include('registration.backends.default.urls')),
]



"""studyportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""