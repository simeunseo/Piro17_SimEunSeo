from django.shortcuts import render
from .models import Review
from django.shortcuts import redirect

def review_list(request):
    reviews = Review.objects.all()
    context = {"reviews": reviews}
    return render(request, template_name='reviews/review_list.html', context=context) 

def review_create(request):
    genres = Review.GENRE_CHOICES
    
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
        
    context = {"genres": genres}
    return render(request, template_name ="reviews/review_create.html", context=context)

def review_detail(request, id):
    review = Review.objects.get(id=id)
    context = {
        "review" : review
    }
    return render(request, template_name="reviews/review_detail.html", context=context)

def review_update(request, id):
    genres = Review.GENRE_CHOICES
    if request.method == "POST":
        title = request.POST["title"]
        year = request.POST["year"]
        genre = request.POST["genre"]
        star = request.POST["star"]
        runtime = request.POST["runtime"]
        review = request.POST["review"]
        director = request.POST["director"]
        actor = request.POST["actor"]
        
        Review.objects.create(title=title, year=year, genre=genre, star=star, runtime=runtime, review=review, director=director, actor=actor)
        return redirect("f/review/{id}")
    
    elif request.method == "GET":
        review = Review.objects.get(id=id)
        context = {
            "review" : review,
            "genres" : genres
        }
        return render(request, template_name="reviews/review_update.html", context=context)