from django.db import models

# Create your models here.

import datetime
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(m)