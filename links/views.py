from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.utils import timezone

# Create your views here.
from .models import *

def create_link(request: HttpRequest):
    if request.method == "POST":
        message = request.POST.get("message")
        expires_in = request.POST.get("expires_in", "")
        is_one_time = "one_time" in request.POST

        new_link = BurnerLink(
            message=message,
            created_at=timezone.now(),
            expires_at=timezone.now() + timezone.timedelta(hours=24),
            is_one_time=is_one_time
        )

        new_link.save()

        return render(request, "created.html", {"link": new_link})
    
    return render(request, "create.html")

def redirect_link(request: HttpRequest, slug):
    link = get_object_or_404(BurnerLink, slug=slug)
    if timezone.now() >= link.expires_at:
        link.delete()
        return render(request, "expired.html")
    
    link.visits += 1
    if link.is_one_time:
        link.delete()
    else:
        link.save()

    return render(request, "created.html", {"link": link})