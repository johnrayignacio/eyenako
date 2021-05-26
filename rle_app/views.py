from django.shortcuts import render

as1 = False
as2 = False
as3 = False
as4 = False

# Create your views here.
def home(request):
    context = {}
    return render(request, 'rle_app/home.html', context)

def reviewer(request):
    context = {}
    return render(request, 'rle_app/reviewer.html', context)

def assessment(request):
    context = {}
    return render(request, 'rle_app/assessments.html', context)

def first_assessment(request):
    context = {}
    return render(request, 'rle_app/assessment1.html')

def second_assessment(request):
    context = {}
    return render(request, 'rle_app/assessment2.html')

def third_assessment(request):
    context = {}
    return render(request, 'rle_app/assessment3.html')

def fourth_assessment(request):
    context = {}
    return render(request, 'rle_app/assessment4.html')