from django  import forms

from .models   import BOOKING

class BookingForm(forms.ModelForm):
    class Meta:
        model = BOOKING
        fields = '__all__'