from multiprocessing import context
from django.shortcuts import render, redirect
from django.views.generic import *
from django.urls import reverse_lazy, reverse

import speakersd
from .models import *
from .forms import *
import random, string, datetime, time
from django.db.models import Q


def generateKey():
    x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(5))
    return x

# Create your views here.
def home(request):
    return render(request, "speakersd/home.html", {"title" : "home"})


class AddSpeaker(View):
    form_class=SpeakerForm
    template_name='speakersd/addspeaker.html'
        
    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form=self.form_class(request.POST,request.FILES)
        print("enter post")
        for field in form:
            print("Field Error:", field.name,  field.errors)
        if form.is_valid():
            print("enters first if")
            provider=form.save(commit=False)
            phone_number=form.cleaned_data["phone_number"]
            if phone_number>=6000000000 and phone_number<=9999999999:
                print("enters second if")
                form.instance.s_id=generateKey()
                #form.instance.avialable_months=','.join(form.cleaned_data['available_months'])
                provider.save()

                #img_object = form.cleaned_data["pic"]  
                #return render(request, 'speakersd/addspeaker.html', {'form': form, 'img_obj': img_object})  
                return redirect("speakersd:home")
            
        else:
            return render(request,self.template_name,{'form':form})

def sl(request):
    context={
        'speakers' : Speaker.objects.all()
    }
    return render(request, 'speakersd/speakerlist.html', context)

class SpeakerListView(ListView):
    model=Speaker
    template_name = 'speakersd/speakerlist.html'
    context_object_name = 'speakers'
    paginate_by = 5

class SpeakerDetailView(DetailView):
    model=Speaker
    template_name = 'speakersd/speakerdetail.html'