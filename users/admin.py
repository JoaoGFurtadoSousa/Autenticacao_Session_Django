from django.contrib import admin
from .models import Users

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'password')
    list_editable = ('username', 'email', )
    search_fields = ('email', )
    list_filter = ('grupo', )

