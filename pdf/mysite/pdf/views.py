from django.shortcuts import render
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io




def index(request):

    if request.method == 'POST':
        name = request.POST.get("name","")
        email = request.POST.get("email","")
        phone = request.POST.get("phone","")
        summary = request.POST.get("summary","")
        degree = request.POST.get("degree","")
        school = request.POST.get("school","")
        university = request.POST.get("univeristy","")
        experience = request.POST.get("experience","")
        skills = request.POST.get("skills","")

        profile = Profile(name=name,email=email,phone=phone,summary=summary,degree=degree,school=school,university=university,previous_work=experience,skills=skills)
        profile.save()

    return render(request,'pdf/forms.html')


def resume(request,id):
    profile = Profile.objects.get(pk=id)

    #extract the template
    template = loader.get_template('pdf/resume.html')
    #pass in the template into the loader
    html = template.render({'profile':profile})

    options = {
        'page-size':"Letter",
        'encoding':'UTF-8',
    }

    pdf = pdfkit.from_string(html,False,options)

    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] = 'attachment'
    filename ='resume.pdf'

    return response
