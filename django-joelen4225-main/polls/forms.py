from django import forms
from .models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['question', 'reporter_name', 'report_text']
        widgets = {'question': forms.HiddenInput()}