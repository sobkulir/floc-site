from django.contrib import admin
from django.contrib.auth.models import User
from django_reverse_admin import ReverseModelAdmin

from .models import Actor


class UserInline(admin.StackedInline):
    model = User
    fields = ['first_name', 'last_name', 'email', ]


class ActorAdmin(ReverseModelAdmin):
    inline_type = 'tabular'
    inline_reverse = [
        ('user', {'fields': ['username', 'first_name', 'last_name', 'email']}),
    ]

admin.site.register(Actor, ActorAdmin)