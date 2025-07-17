from django.http import HttpResponse
from django.shortcuts import render
import pathlib
from visits.models import PageVisit

# This is the directory where this file is located
this_dir = pathlib.Path(__file__).parent.resolve()

def home_view(request, *args, **kwargs):
    return about_view(request, *args, **kwargs)

def  about_view(request , *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs =  PageVisit.objects.filter(path = request.path)

    try:
        percent = (page_qs.count()  * 100) / qs.count()
    except ZeroDivisionError:
        percent = 0

    my_title = "my page title"
    html_template = "home.html"

    my_context = {
        "page_title": my_title,
        "page_visit_count": page_qs.count(),
        "total_visit_count": qs.count(),
        "percent": percent,
    }
    html_ = ""
    path = request.path
    html_template = "home.html"
    PageVisit.objects.create(path =request.path)

    return render(request, html_template, my_context)


def my_old_home_page_view(request, *args, **kwargs):
    print(this_dir)
    my_title = "my page title"
    my_context = {
        "page_title": my_title,
    }
    html_ = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <title>{my_context['page_title']}</title>
</head>
<body>
    <h1>{my_context['page_title']}</h1>
</body>
</html>
""".format(**my_context)
    # html_file_path = this_dir / "home.html"
    # html_ = html_file_path.read_text()
    return HttpResponse(html_)