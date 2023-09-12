from django.contrib import admin

from .models import HighLevel, Questionnaire

@admin.register(HighLevel)
class HighAdmin(admin.ModelAdmin):
    list_display = ['h_id', 'name']
    readonly_fields = ("h_id","created_at")
    fieldsets = [
        ('Data', {
            'fields':('h_id', 'name', 'is_active', 'description', 'created_at')
        })
        ]

@admin.register(Questionnaire)
class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = ['questionnaire_id', 'user_email', 'created_at' ]
    readonly_fields = ("questionnaire_id","created_at", 'updated_at')
    fieldset = [
        ('data', {
            'fields':('questionnaire_id', 'created_at', 'updated_at', 'user_email', 'often_injury', 'step')
        }),
    ]