from django.shortcuts import render, get_object_or_404, redirect
from .models import Idea
from .forms import IdeaForm
from datetime import datetime

def main(request):
    return render(request, template_name='ideas/main.html')

def register(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST)
        if form.is_valid():
            idea = form.save(commit=False)
            idea.save()
            return redirect('')
        else :
            return redirect('')
    else :
        form = IdeaForm()
        return render(request, 'ideas/register.html', {'form' : form})