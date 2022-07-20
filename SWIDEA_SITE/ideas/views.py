import json
from django.shortcuts import render, get_object_or_404, redirect
from .models import Idea, Tool
from .forms import IdeaForm, ToolForm
from datetime import datetime
from django.http import HttpResponse,JsonResponse


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
            return redirect('/')
        else :
            return redirect('/')
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
        context = {
            "idea" : idea,
            "form" : form
        }
        return render(request, 'ideas/edit.html', context=context)

def delete(request, id):
    if request.method == "POST":
        idea = Idea.objects.get(id=id)
        idea.delete()
    return redirect('/')

def tool(request):
    tools = Tool.objects.all()
    context = {
        "tools" : tools
    }
    return render(request, template_name='ideas/tool.html', context=context)

def tool_register(request):
    if request.method == 'POST':
        form = ToolForm(request.POST)
        if form.is_valid():
            tool = form.save(commit=False)
            tool.save()
            return redirect('/tool')
        else :
            return redirect('/tool')
    else :
        form = ToolForm()
        return render(request, 'ideas/tool_register.html', {'form' : form})
    
def tool_detail(request,id):
    tool = Tool.objects.get(id=id)
    ideas = Idea.objects.all()
    for idea in ideas:
        print(idea.tool.name)
    context = {
        "tool":tool,
        "ideas":ideas,
    }
    return render(request, template_name="ideas/tool_detail.html",context=context)

def tool_edit(request, id):
    tool = get_object_or_404(Tool, id=id)

    if request.method == "POST":
        form = ToolForm(request.POST, instance=tool)
        if form.is_valid():
            tool = form.save()
            tool.save()
        return redirect(f'/tool/detail/{id}')
    else:
        form = ToolForm(instance=tool)
        context = {
            "tool" : tool,
            "form" : form
        }
        return render(request, 'ideas/tool_edit.html', context=context)
    
def tool_delete(request, id):
    if request.method == "POST":
        tool = Tool.objects.get(id=id)
        tool.delete()
    return redirect('/tool')

def likes(request): 
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        idea_id = request.GET['idea_id'] 
        idea = Idea.objects.get(id=idea_id) 
				
        if not request.user.is_authenticated: #버튼을 누른 유저가 비로그인 유저일 때
            message = "로그인을 해주세요"
            context = {'like_count' : idea.like.count(),"message":message}
            return HttpResponse(json.dumps(context), content_type='application/json')

        user = request.user #request.user : 현재 로그인한 유저
        if idea.like.filter(id = user.id).exists():
            idea.like.remove(user) 
            message = "좋아요 취소" 
        else: 
            idea.like.add(user) 
            message = "좋아요" 

        context = {'like_count' : idea.like.count(),"message":message}
        return HttpResponse(json.dumps(context), content_type='application/json')