# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Profileteacher, Profilechild, Profileparent, Profileparent, Attendance, Mcqs, Resources, Assignments, Question, Univresults

# Register your models here.

admin.site.register(Profileteacher)

admin.site.register(Profilechild)

admin.site.register(Profileparent)

admin.site.register(Attendance)

admin.site.register(Mcqs)

admin.site.register(Resources)

admin.site.register(Assignments)

admin.site.register(Univresults)
