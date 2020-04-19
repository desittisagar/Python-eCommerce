from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ContactForm(forms.Form):
	fullname	= forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
	email		= forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}))
	content		= forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))


	def clean_email(self):			# for custom validation use "clean_" field name
		email = self.cleaned_data.get("email")
		if "gmail.com" not in email:
			raise forms.ValidationError("email must contain gmail.com")
		return email


class Loginform(forms.Form):
	username	= forms.CharField()
	password	= forms.CharField(widget = forms.PasswordInput())	


class Registerform(forms.Form):
	username	= forms.CharField()
	email		= forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}))
	password	= forms.CharField(widget = forms.PasswordInput())
	password2	= forms.CharField(widget = forms.PasswordInput())

	def clean_username(self):
		username = self.cleaned_data.get("username")
		qs = User.objects.filter(username = username)
		if qs.exists():
			raise forms.ValidationError("username already taken")

	def clean(self):
		password = self.cleaned_data.get("password")
		password2 = self.cleaned_data.get("password2")
		#print("username", self.cleaned_data.get("username"))

		if password != password2:
			raise forms.ValidationError("password must match")
		else:
			return self.cleaned_data	