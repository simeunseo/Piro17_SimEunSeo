from django.conf import settings
from django.db import models
from django.utils import timezone

class Review(models.Model):
    #영화제목, 개봉년도, 장르, 별점, 러닝타임, 리뷰, 감독, 배우
    title = models.CharField(max_length=50, verbose_name="제목")
    release_year = models.CharField(max_length=4, verbose_name="개봉년도")
    GENRE_CHOICES = (
        ('ACTION','액션'),
        ('CRIME','범죄'),
        ('SF','SF'),
        ('COMEDY','코미디'),
        ('ROMANCE','로맨스'),
        ('ROMANCE-COMEDY','로맨스 코미디'),
        ('BLACK-COMEDY','블랙 코미디'),
        ('THRILLER','스릴러'),
        ('HORROR','공포'),
        ('WAR','전쟁'),
        ('FANTASY','판타지'),
        ('MUSIC','음악'),
        ('HISTORICAL','역사'),
        ('DRAMA','드라마'),
        ('DOCUMENTARY','다큐멘터리'),
    )
    genre = models.CharField(max_length=2, choices=GENRE_CHOICES, verbose_name="장르")
    star = models.DecimalField(max_digits=2, decimal_places=1, verbose_name="별점")
    runtime = models.IntegerField(max_length=50, verbose_name="러닝타임")
    review = models.TextField(verbose_name="리뷰")
    director = models.CharField(max_length=50, verbose_name="감독")
    actor = models.CharField(max_length=50, verbose_name="배우")