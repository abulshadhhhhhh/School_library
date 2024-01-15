from django.contrib import admin
from.models import Register,Issue,Book
# Register your models here.
admin.site.register(Register)
# admin.site.register(Login)
admin.site.register(Book)
admin.site.register(Issue)