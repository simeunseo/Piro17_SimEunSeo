from django.shortcuts import render
from .models import Review
from django.shortcuts import redirect

def review_list(request):
    reviews = Review.objects.all()
    context = {"reviews": reviews}
    return render(request, template_name='reviews/review_list.html', context=context) 

def review_create(request):
    if request.method == 'POST':
        # post 요청 값 받기 
        title = request.POST["title"]
        year = request.POST["year"]
        genre = request.POST["genre"]
        star = request.POST["star"]
        runtime = request.POST["runtime"]
        review = request.POST["review"]
        director = request.POST["director"]
        actor = request.POST["actor"]

        # 데이터 베이스에 저장하기 
        Review.objects.create(title=title, year=year, genre=genre, star=star, runtime=runtime, review=review, director=director, actor=actor)
        return redirect("/review")
        
    context = {}
    return render(request, template_name ="reviews/review_create.html", context=context)