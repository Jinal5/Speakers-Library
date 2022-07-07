from django import forms
from django.forms import ClearableFileInput
from .models import *

AvailMonth=[
    ('NON','Unavailable'),
    ('JAN','January'),
    ('FEB','February'),
    ('MAR','March'),
    ('APR','April'),
    ('MAY','May'),
    ('JUN','June'),
    ('JUL','July'),
    ('AUG','August'),
    ('SEP','September'),
    ('OCT','October'),
    ('NOV','November'),
    ('DEC','December'),
]

class SpeakerForm(forms.ModelForm):
    #available_months = forms.MultipleChoiceField(choices = AvailMonth,widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Speaker
        fields = [
            "name_of_speaker",
            "pic",
            "address_citycountry",
            "phone_number",
            "email_id",
            "profession",
            "awards",
            "desc",
            "books",
            #"available_months",
            "upcoming_events",
        ]
       
        exclude = ('s_id','upload_date','available_months')

        #def clean_avilable_months(self):
        #    return ','.join(self.cleaned_data['available_months'])