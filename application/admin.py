from django.contrib import admin
from .models import RegisterUser,userQuestion

# Register your models here.

admin.site.register(RegisterUser)

@admin.register(userQuestion)
class userQuestionAdmin(admin.ModelAdmin):
    list_display = ["title","category","queriedBy"]