# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, user_passes_test
from sappsapp.models import Profileteacher, Profilechild, Profileparent, Mcqs, Question, Assignments, Resources, Univresults, Attendance
from sappsapp.forms import ProfileteacherForm, AttendanceForm, McqsForm, QuestionForm, AssignmentsForm, ResourcesForm, UnivresultsForm
from datetime import date
# Create your views here.


def index(request):
	return render(request, 'index.html', context=None)


def login(request):
	return render(request, 'login.html', context=None)

@login_required
def dashboard(request):
	if request.user.is_authenticated():
		try:
			profile = Profileteacher.objects.get(user=request.user, user__is_active = True)
		except:
			profile = None
	return render(request, 'dashboard.html', {'profile':profile})

@login_required
def profile(request):
	if request.user.is_authenticated():
		try:
			profile = Profileteacher.objects.get(user=request.user, user__is_active = True)
		except:
			profile = None
	return render(request, 'dashboard/profile.html', {'profile':profile})

@login_required
def profileedit(request):
	try:
		profile = Profileteacher.objects.get(user=request.user, user__is_active = True)
	except:
		profile = None
	if request.method == "POST":
		form = ProfileteacherForm(request.POST, instance=profile)
		if form.is_valid():
			profile = form.save(commit=False)
			profile.user = request.user
			profile.save()
			return redirect('profile')
	else:
		form = ProfileteacherForm(instance=profile)
	return render(request, 'dashboard/profileedit.html', {'form':form, 'profile':profile })


@login_required
def students(request):
	if request.user.is_authenticated():
		try:
			profile = Profileteacher.objects.get(user=request.user, user__is_active = True)
			childprofile = Profilechild.objects.all()
		except:
			profile = None
			childprofile =None
	return render(request, 'dashboard/students.html', {'profile':profile, 'childprofile':childprofile})


@login_required
def attendance(request):
	today=date.today()
	if request.user.is_authenticated():
		try:
			profile = Profileteacher.objects.get(user=request.user, user__is_active = True)
			attend = Attendance.objects.filter(day=today)
		except:
			profile = {}
			attend = {}
	if request.method == "POST":
		form = AttendanceForm(request.POST)
		if form.is_valid():
			att = form.save(commit=False)
			att.save()
			return redirect('attendance')
	else:
		form = AttendanceForm()
	return render(request, 'dashboard/attendance.html', {'profile':profile, 'form':form, 'attend':attend })


@login_required
def mcqs(request):
	if request.user.is_authenticated():
		try:
			profile = Profileteacher.objects.get(user=request.user, user__is_active = True)
			mcqs = Mcqs.objects.get(user=request.user)
		except:
			profile = None
			mcqs = None
	if request.method == "POST":
		form = McqsForm(request.POST)
		if form.is_valid():
			att = form.save(commit=False)
			att.user = request.user
			att.marks = 0
			att.save()
		return redirect('setmcq')
	else:
		form = McqsForm()
	return render(request, 'dashboard/setmcq.html', {'profile':profile, 'mcqs':mcqs, 'form':form })


@login_required
def assignments(request):
	user = request.user
	if request.user.is_authenticated():
		try:
			profile = Profileteacher.objects.get(user=user, user__is_active = True)
			assigns = Assignments.objects.filter(user=user)
		except:
			profile = {}
			assigns = {}
	if request.method == "POST":
		form = AssignmentsForm(request.POST, request.FILES)
		if form.is_valid():
			forms = form.save(commit=False)
			forms.user = user
			forms.save()
			return redirect('assignments')
	else:
		form = AssignmentsForm()
	return render(request, 'dashboard/assignments.html', { 'profile':profile, 'assigns':assigns, 'form':form, })


@login_required
def resources(request):
	user = request.user
	if request.user.is_authenticated():
		try:
			profile = Profileteacher.objects.get(user=user, user__is_active = True)
			res = Resources.objects.filter(user=user)
		except:
			profile = {}
			res ={}
	if request.method == "POST":
		form = ResourcesForm(request.POST, request.FILES)
		if form.is_valid():
			formres = form.save(commit=False)
			formres.user = user
			formres.save()
			return redirect('resources')
	else:
		form = ResourcesForm()
	return render(request, 'dashboard/resources.html', { 'profile':profile, 'res':res, 'form':form, })
