from django.contrib import admin
from accounts.models import User, Profile

# Register your models here.


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'height', 'weight', 'age']

admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
