from django.db import models
from multiselectfield import MultiSelectField
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator

# Create your models here.

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

class Speaker(models.Model):
    s_id=models.CharField(max_length=5, unique=True, blank=True,null=True)
    name_of_speaker=models.CharField(max_length=400)
    pic=models.ImageField(upload_to="images", null=True, blank=True)
    address_citycountry=models.CharField(max_length=500)
    phone_number=models.BigIntegerField(null=True, blank=True)
    email_id=models.EmailField(max_length=254)
    profession=models.CharField(max_length=500)
    awards=models.TextField(blank=True)
    desc=models.TextField()
    books=models.TextField()
    available_months=models.CharField(choices=AvailMonth,max_length=3,null=True)
    upcoming_events=models.CharField(max_length=400, blank=True)
    upload_date=models.DateField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.s_id
