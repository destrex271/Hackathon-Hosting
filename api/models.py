from django.db import models
from django.db.models.base import Q, CheckConstraint

# Create your models here.

SUBMISSION_TYPES = (("1", "image"), ("2", "file"), ("3", "link"))


class Hackathon(models.Model):
    title               = models.CharField(max_length=100, null=False, blank=True)
    description         = models.CharField(max_length=1000, null=False, blank=True)
    background_image    = models.ImageField(upload_to='images')
    hackathon_image     = models.ImageField(upload_to='images')
    submission_type     = models.CharField(choices=SUBMISSION_TYPES)
    start_date          = models.DateField(blank=False)
    end_date            = models.DateField(blank=False)
    # Constraint Check for dates
    CheckConstraint(check=Q(start_date < end_date), name="date_conf")


class Rewards(models.Model):
    hackathon           = models.ForeignKey(to="Hackathon", on_delete=models.CASCADE)
    prize_type          = models.CharField(max_length=100)
    monetary_value      = models.IntegerField()
    prize_desc          = models.TextField(default="")


class Submission(models.Model):
    name                = models.CharField(max_length=100)
    summary             = models.TextField()
    submission_image    = models.ImageField('submitted')
    submission_file     = models.FileField()
    submission_link     = models.URLField()
    hackathon           = models.ForeignKey(to="Hackathon", on_delete=models.CASCADE)
    participant         = models.ForeignKey(to='Participant', on_delete=models.CASCADE)


class Participant(models.Model):
    hackathon           = models.ForeignKey(to='Hackathon', on_delete=models.CASCADE)
    user                = models.ForeignKey(to='users.CustomUser', on_delete=models.CASCADE)
