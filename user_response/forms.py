from django import forms
from .models import User_data


class userResponseForm(forms.ModelForm):
	class Meta:
		model = User_data
		fields = ['person_name', 'person_mobile','date']
