from django.shortcuts import render, get_object_or_404, redirect, render_to_response

def home(request):
    return render_to_response("app/index.html")

