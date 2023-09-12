from django.db import models


class Questionnaire(models.Model):
    questionnaire_id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_email = models.EmailField(max_length=100, blank=True)
    weigh = models.DecimalField(max_digits=4, decimal_places=1, default=60)
    injury = models.BooleanField(default=False)
    training = models.BooleanField(default=False)
    often_injury = models.CharField(choices=[
        ("OM", "one on mounth"),
        ("OY", "one on year"),
        ("O5", "one on 5 years"),
        ("NI", "i don't have injury"),
    ], default="NI", max_length=255)
    often_training = models.CharField(choices=[
        ("OM", "one on mounth"),
        ("OY", "one on year"),
        ("O5", "one on 5 years"),
        ("NI", "i don't have training"),
    ], default="NI", max_length=255)
    
    def __int__(self):
        return f'questionnaire id: {self.questionnaire_id}'
    



class HighLevel(models.Model):
    h_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    #objectives - list

class MediumLevel(models.Model):
    m_id = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    #objectives - list

class LowLevel(models.Model):
    l_id = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    #objectives - list

