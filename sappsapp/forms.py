from django import forms
from .models import Profileteacher, Attendance, Mcqs, Question, Assignments, Resources, Univresults
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProfileteacherForm(forms.ModelForm):
    class Meta:
        model = Profileteacher
        fields = ('phone','email','gender','department','qualification','about','address','picture')


CHOICES=[('student','student'),('parent','parent')]


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields =('user','day','status')


class McqsForm(forms.ModelForm):
    class Meta:
        model = Mcqs
        fields = ('test_id','name')

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('mcq','question', 'c1', 'c2', 'c3', 'c4', 'options', 'answer', 'marks')


class UnivresultsForm(forms.ModelForm):
    class Meta:
        model = Univresults
        fields = ('sub1','mark1','intern1','res1','max1','intern1max','total1','total',)


class AssignmentsForm(forms.ModelForm):
    class Meta:
        model = Assignments
        fields = ('topic','disc','fil',)


class ResourcesForm(forms.ModelForm):
      class Meta:
            model = Resources
            fields = ('topic','disc','video',)
