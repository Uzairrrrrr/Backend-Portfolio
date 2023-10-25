from django.shortcuts import render
from .models import About, Work, Education, Services, WorkDone, Testimonials, CV_link

def Portfolio(request):
    about_data = About.objects.all()
    work_data = Work.objects.all()
    education_data = Education.objects.all()
    services_data = Services.objects.all()
    work_done_data = WorkDone.objects.all()
    testimonials_data = Testimonials.objects.all()
    CV_link_data = CV_link.objects.all()
    params = {'about_data': about_data, 'work_data': work_data, 'education_data': education_data, 'services_data': services_data, 'work_done_data': work_done_data, 'testimonials_data': testimonials_data, 'CV_link_data': CV_link_data,}
    return render(request, 'Api/index.html', params)