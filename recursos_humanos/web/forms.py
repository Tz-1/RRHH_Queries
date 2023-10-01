from django import forms

from web.models import *

class ChoiceForm(forms.Form):
    select_businessid = forms.ModelChoiceField(
        queryset=Person.objects.all().order_by('businessentityid'),
        to_field_name='businessentityid',
        label="Business ID",
        widget=forms.Select(attrs={'class': 'form-select'}),
        required=False,
        empty_label="Choose the ID of the Person"
    )
   
    select_jobtitle = forms.ModelChoiceField(
        queryset=Employee.objects.all().distinct('jobtitle').order_by('jobtitle'),
        to_field_name='jobtitle', label="Job Title", 
        widget=forms.Select(attrs={'class':'form-select'}), 
        required=False, 
        empty_label="Choose the Job Title"
    )
    
    CHOICES = [
        ('', ''),
        ('M', 'M'),
        ('F', 'F')]
    
    select_gender = forms.ChoiceField(
        choices = CHOICES,
        label="Gender", 
        widget=forms.Select(attrs={'class':'form-select'}), 
        required=False, 
    )

