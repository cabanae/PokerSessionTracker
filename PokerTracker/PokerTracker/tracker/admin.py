from django.contrib import admin
from .models import Session, Place, Game
from django.contrib.auth.models import User

admin.site.register(Game)
admin.site.register(Place)
class SessionsInline(admin.TabularInline):
    """
    Defines format of inline book insertion (used in AuthorAdmin)
    """
    model = Session


#@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    """
    Administration object for Session models.
    """

    list_display = ('session_user','time_start', 'time_end','amount','place','Notes')

class SessionAdmin(admin.ModelAdmin):
    list_display = ('session_user', 'time_start', 'time_end', 'amount', 'place', 'Notes')
    def save_model(self, request, obj, form, change):
        if not change:
            obj.session_user = request.user
        obj.save()

admin.site.register(Session, SessionAdmin);