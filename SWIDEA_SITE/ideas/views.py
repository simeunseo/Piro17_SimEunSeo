from django.shortcuts import render, get_object_or_404, redirect
from .models import Idea
from .forms import IdeaForm
from datetime import datetime

def main(request):
    ideas = Idea.objects.all()
    context = {
        "ideas" : ideas
    }
    return render(request, template_name='ideas/main.html', context=context)

def register(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            idea = form.save(commit=False)
            idea.save()
            return redirect('')
        else :
            return redirect('')
    else :
        form = IdeaForm()
        return render(request, 'ideas/register.html', {'form' : form})

def detail(request, id):
    idea = Idea.objects.get(id=id)
    context = {
        "idea":idea,
    }
    return render(request, template_name="ideas/detail.html",context=context)

def edit(request, id):
    idea = get_object_or_404(Idea, id=id)
    if request.method == "POST":
        form = IdeaForm(request.POST, request.FILES, instance=idea)
        if form.is_valid():
            idea = form.save()
            idea.save()
            return redirect(f'/detail/{id}')
    else:
        form = IdeaForm(instance=idea)
    return render(request, 'ideas/register.html',{'form' : form})