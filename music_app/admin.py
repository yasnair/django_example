from django.contrib import admin
from .models import UserAdmin, PlaylistAdmin, User, Playlist


# Register your models here.
#admin.site.register(models.User)
#admin.site.register(models.Playlist)


admin.site.register(User, UserAdmin)
admin.site.register(Playlist, PlaylistAdmin)
