from django.http import HttpResponse

def home(request):
    return HttpResponse("Modular Vendor Product Course Certification API is running")