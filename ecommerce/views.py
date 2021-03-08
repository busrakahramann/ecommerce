from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render, redirect

from .forms import ContactForm
from products.models import Product

def home_page(request):
    context = {
        "title":"HELLO WORLD!",
        "content":" Welcome to the homepage",
    }
    if request.user.is_authenticated:
        context["premium_content"] = "YEAHHHHH"
    return render(request, "products/list.html", context)

def about_page(request):
    context = {
        "title": "ABOUT PAGE",
        "content":" Welcome to the aboutpage"
    }
    return render(request, "home_page.html", context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
         "title": "Contact",
         "content":" Welcome to the contactpage",
         "form": contact_form,

    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
        if request.is_ajax():
            return JsonResponse({"message":"Thank you for your submission"})

    if contact_form.errors:
        errors = contact_form.errors.as_json()
        if request.is_ajax():
             return HttpResponse(errors, status=400, content_type='application/json')

    return render(request, "contact/view.html", context)


def home_page_old(request):
    html_ = """
    <!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">

    <title>Hello, world!</title>
  </head>
  <body>
    <div class='text-center'>
        <h1>Hello, world!</h1>
    </div>
    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: Bootstrap Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>

    <!-- Option 2: Separate Popper and Bootstrap JS -->
    <!--
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js" integrity="sha384-q2kxQ16AaE6UbzuKqyBE9/u/KzioAlnx2maXQHiDX9d4/zp8Ok3f+M7DPm+Ib6IU" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.min.js" integrity="sha384-pQQkAEnwaBkjpqZ8RU1fF1AKtTcHJwFl3pblpTlHXybJjHpMYo79HY3hIi4NKxyj" crossorigin="anonymous"></script>
    -->
  </body>
</html>
    """
    return HttpResponse(html_)