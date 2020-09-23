from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    # 학번, 이름, 비밀번호
    student_id = models.CharField(max_length = 10)
    name = models.CharField(max_length = 10)
    pw = models.CharField(max_length = 10)

