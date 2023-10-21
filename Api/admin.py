from django.contrib import admin
from .models import  About, Work, Education, Services, WorkDone, Testimonials


class AboutAdmin(admin.ModelAdmin):
    list_display = ('content1', 'content2', 'content3', 'content4')

admin.site.register(About, AboutAdmin)
# verbos_name = "About"

class WorkAdmin(admin.ModelAdmin):
    list_display = ('date', 'heading', 'content')

admin.site.register(Work, WorkAdmin)

class EducationAdmin(admin.ModelAdmin):
    list_display = ('date', 'heading', 'content')

admin.site.register(Education, EducationAdmin)

class ServicesAdmin(admin.ModelAdmin):
    list_display = ('heading', 'content')

admin.site.register(Services, ServicesAdmin)

class WorkDoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'content')

admin.site.register(WorkDone, WorkDoneAdmin)

class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'content')

admin.site.register(Testimonials, TestimonialsAdmin)