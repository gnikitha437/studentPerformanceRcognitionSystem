from django import forms
from .models import Student, Achievement
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'batch', 'gpa', 'core_course_score', 'hackathon_score', 'paper_presentation_score', 'teaching_assistance_score']

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Save Student'))

class AchievementForm(forms.ModelForm):
    class Meta:
        model = Achievement
        fields = ['student', 'achievement_type', 'score', 'date']

    def __init__(self, *args, **kwargs):
        super(AchievementForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Save Achievement'))