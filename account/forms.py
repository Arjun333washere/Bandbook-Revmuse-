from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


from band.models import Band
from django import forms
from django.forms import ModelForm
#from .models import Band

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_admin', 'is_employee', 'is_customer')



class BandForm(ModelForm):
	class Meta:
		model = Band 
		fields = ('band_name','band_price', 'description','img', 'genres','band_number','band_address','band_location','band_email')
		labels = {
			'band_name': '',
			'band_address': '',
			'band_price': '',
			'band_number': '',
			'description': '',
			'band_email': '',
			'band_location': '',	
            'img': '',
            'genres': '',	

		}
		widgets = {
			'band_name': forms.TextInput(attrs={'class':'form-row form-row-1', 'placeholder':'Band Name'}),
			'band_address': forms.TextInput(attrs={'class':'form-row', 'placeholder':'Address'}),
			'band_price': forms.TextInput(attrs={'class':'form-control', 'placeholder':'price'}),
            'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'description'}),
			'band_number': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone'}),
			'band_email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
            'band_location': forms.TextInput(attrs={'class':'form-control', 'placeholder':'location'}),
            #'img': forms.
            #'genres': forms.

		}