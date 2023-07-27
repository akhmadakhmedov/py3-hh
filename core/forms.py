from django import forms
from .models import Vacancy, Company

class VacancyForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    class Meta:
        model = Vacancy
        fields = ['title', 'salary', 'description', 'email', 'contacts']


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = "__all__"

class VacancyEditForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields =['title', 'salary', 'description', 'email', 'contacts']