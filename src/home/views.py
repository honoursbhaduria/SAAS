from django.http import HttpResponse

def home_page_views(request):
    return HttpResponse("Hello, fuck  world")

