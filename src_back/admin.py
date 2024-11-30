# admin.py
from django.contrib import admin

from src_back.models import User, LoginToken

admin.site.register(User)
admin.site.register(LoginToken)
