from django import forms


class JobForm(forms.Form):
    company_name = forms.CharField(max_length=200)
    jobposter_email = forms.EmailInput()
    
