from django.shortcuts import render
from .models import Review

# reviews = Review.objects.all()
# print(reviews)

def review_list(request):
    reviews = Review.objects.all()
    context = {"reviews": reviews}
    return render(request, template_name='reviews/review_list.html', context=context) 