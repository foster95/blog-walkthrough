from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import About
from django.contrib import messages
from .forms import CollaborateForm

def about_me(request):
    """
    Display the About Me page.

    **Context**

    ``about``
        An instance of :model:`about.About`.

    **Template:**

    :template:`about/about_me.html`
    """
    about = About.objects.all().order_by('-updated_on').first()
    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_request = collaborate_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Collaboration request received! ' 
                'I endeavour to respond within 2 working days.'
            )
    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {"about": about, 
         "collaborate_form": collaborate_form},
    )

