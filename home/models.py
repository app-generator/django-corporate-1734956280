# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    user = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(max_length=255, null=True, blank=True)
    experience_points = models.IntegerField(null=True, blank=True)
    digital_portfolio = models.CharField(max_length=255, null=True, blank=True)
    profile_picture = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Company(models.Model):

    #__Company_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    contact_email = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Company_FIELDS__END

    class Meta:
        verbose_name        = _("Company")
        verbose_name_plural = _("Company")


class Challenge(models.Model):

    #__Challenge_FIELDS__
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    reward_points = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    deadline = models.DateTimeField(blank=True, null=True, default=timezone.now)
    participants = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    #__Challenge_FIELDS__END

    class Meta:
        verbose_name        = _("Challenge")
        verbose_name_plural = _("Challenge")


class Userprofile(models.Model):

    #__Userprofile_FIELDS__
    user = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(max_length=255, null=True, blank=True)
    experience_points = models.IntegerField(null=True, blank=True)
    digital_portfolio = models.CharField(max_length=255, null=True, blank=True)
    profile_picture = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Userprofile_FIELDS__END

    class Meta:
        verbose_name        = _("Userprofile")
        verbose_name_plural = _("Userprofile")


class Challengesubmission(models.Model):

    #__Challengesubmission_FIELDS__
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    submission_file = models.CharField(max_length=255, null=True, blank=True)
    submitted_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    feedback = models.TextField(max_length=255, null=True, blank=True)
    score = models.IntegerField(null=True, blank=True)

    #__Challengesubmission_FIELDS__END

    class Meta:
        verbose_name        = _("Challengesubmission")
        verbose_name_plural = _("Challengesubmission")


class Job(models.Model):

    #__Job_FIELDS__
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    requirements = models.TextField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    deadline = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Job_FIELDS__END

    class Meta:
        verbose_name        = _("Job")
        verbose_name_plural = _("Job")


class Jobapplication(models.Model):

    #__Jobapplication_FIELDS__
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    cover_letter = models.TextField(max_length=255, null=True, blank=True)
    resume = models.TextField(max_length=255, null=True, blank=True)
    applied_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    status = models.CharField(max_length=255, null=True, blank=True)

    #__Jobapplication_FIELDS__END

    class Meta:
        verbose_name        = _("Jobapplication")
        verbose_name_plural = _("Jobapplication")


class Connection(models.Model):

    #__Connection_FIELDS__
    from_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    to_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    connected_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    status = models.CharField(max_length=255, null=True, blank=True)

    #__Connection_FIELDS__END

    class Meta:
        verbose_name        = _("Connection")
        verbose_name_plural = _("Connection")


class Portfolio(models.Model):

    #__Portfolio_FIELDS__
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    projects = models.TextField(max_length=255, null=True, blank=True)
    achievements = models.TextField(max_length=255, null=True, blank=True)
    skills = models.TextField(max_length=255, null=True, blank=True)
    updated_at = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Portfolio_FIELDS__END

    class Meta:
        verbose_name        = _("Portfolio")
        verbose_name_plural = _("Portfolio")



#__MODELS__END
