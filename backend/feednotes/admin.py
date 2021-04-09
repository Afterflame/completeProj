from django.contrib import admin


class NoteAdmin(admin.ModelAdmin):
    readonly_fields = ['author']

    def get_form(self, request, obj=None, **kwargs):
        Note.author = request.user.username
        return super().get_form(request, obj, **kwargs)


    def save_model(self, request, obj, form, change):
        obj.author = request.user.username
        obj.author_id = request.user.id
        obj.last_modified_by = request.user
        obj.save()


from .models import Note
admin.site.register(Note, NoteAdmin)