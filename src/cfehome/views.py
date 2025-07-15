from django.http import HttpResponse
from django.shortcuts import render
import pathlib

this_dir = pathlib.Path(__file__).parent.resolve()

def home_page_view(request, *args, **kwargs):
    print(this_dir)
    my_title = "my page title"
    my_context = {
        "page_title": my_title,
    }
    html_ = "" 
    html_template = "home.html"
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