from django.http import HttpResponse
from django.shortcuts import render
import pathlib
from visits.models import PageVisit

# This is the directory where this file is located
this_dir = pathlib.Path(__file__).parent.resolve()

def home_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        print(request.user.username)
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

VALID_CODE = "abcd1234  "

# def pw_protected_view(request, *args, **kwargs):
#     is_allowed = False
#     if request.method == "POST":
#         user_pw = request.POST.get("code") or None
#         if user_pw == VALID_CODE:
#             is_allowed = True

#     if is_allowed:
#         return render(request, "protected/view.html", {})
#     return render(request, "protected/entry.html", {})
def pw_protected_view(request, *args, **kwargs):
    is_allowed = request.session.get('protected_page_allowed') or 0
    print(
        request.session.get('protected_page_allowed'),
        type(request.session.get('protected_page_allowed'))
    )
    if request.method == "POST":
        user_pw_sent = request.POST.get("code") or None
        if user_pw_sent == VALID_CODE:
            is_allowed = 1
            request.session['protected_page_allowed'] = is_allowed
    if is_allowed:
        return render(request, "protected/view.html")
    return render(request, "protected/entry.html")
