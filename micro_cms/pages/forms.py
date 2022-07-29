from django import forms

from leads.models import Lead
from products.models import Country, City


class LeadCaptureForm(forms.ModelForm):

    class Meta:
        model = Lead
        fields = [
            'name',
            'phone_number',
            'email',
            'country',
            'city',
            'address',
            'referral_code'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['country'] = forms.ModelChoiceField(queryset=Country.objects.all())
        self.fields['city'] = forms.ModelChoiceField(queryset=City.objects.all())

