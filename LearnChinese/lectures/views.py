from django.shortcuts import render
from .models import Reading, Listening


# Create your views here.
def courses_home(request):
    return render(request, 'lectures/courses_home.html')


def reading_lessons(request):
    readings = Reading.objects.all()
    context = {"readings": readings}
    return render(request, 'lectures/reading_lessons.html', context)


def listening_lessons(request):
    l_lessons = Listening.objects.all()
    context = {"l_lessons": l_lessons}
    return render(request, 'lectures/listening_lessons.html', context)
