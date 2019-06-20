from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from tagging.fields import TagField


class User(AbstractUser):
    # name = models.CharField(max_length=20)
    number = models.CharField(max_length=20)
    nickname = models.CharField(blank=True, max_length=20)
    user_image = models.ImageField(upload_to='userImages/%Y/%m/%d',default='no_image.png', blank=True)
    temp_number = models.CharField(max_length=20, default='0')
    isStudent = models.BooleanField(default=True, blank=False)


class StoreInfo(models.Model):
    st_name = models.CharField(max_length=40)
    st_number = models.CharField(max_length=20, blank=True)
    st_address = models.TextField(blank=False)
    st_score = models.CharField(max_length=10, default='0')
    tag = TagField()
    review_count = models.IntegerField(default='0')
    latitude = models.CharField(max_length=20, blank=True)
    longitude = models.CharField(max_length=20, blank=True)
    st_time = models.CharField(max_length=200, blank=True)
    category = models.CharField(max_length=50)
    st_image = models.ImageField(upload_to='storeImages',default='no_image.png')

    class Meta:
        ordering = ['-st_score']

    def __str__(self):
        return self.st_name


class Review(models.Model):
    # related_name : 속성값 -> 나중에 user이름.review 라고 쓰면 이 정보를 볼 수 있음
    user_name = models.ForeignKey(get_user_model(),on_delete=models.CASCADE, related_name='rev')
    store = models.ForeignKey(StoreInfo, on_delete=models.CASCADE, related_name='rev', default='0')
    review_score = models.FloatField(default='1.0')
    text = models.TextField(blank=True)
    hearts = models.IntegerField(default='0', blank=False)
    review_image = models.ImageField(upload_to='reviewImages/%Y/%m/%d', default='no_image.png')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        reviews = self.store.rev.all()
        count = len(reviews) + 1

        score = sum(map(lambda x: x.review_score, reviews)) + self.review_score
        avg = score/count
        if 0 < avg and avg < 1.0:
            avg = 0.0
        elif 1.0 <= avg and avg < 2.0:
            avg = 1.0
        elif 2.0 <= avg and avg < 3.0:
            avg = 2.0
        elif 3.0 <= avg and avg <= 4.0:
            avg = 3.0
        elif 4.0 <= avg and avg < 5.0:
            avg = 4.0
        else:
            avg = 5.0


        self.store.st_score = avg
        self.store.review_count = count
        self.store.save()

        super(Review,self).save(force_insert, force_update,using,update_fields)

class SchoolAdressBook(models.Model):
    team_name = models.CharField(max_length=30, blank=True)
    name = models.CharField(max_length=30,blank=False)
    number = models.CharField(max_length=30)