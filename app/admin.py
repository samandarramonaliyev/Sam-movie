from django.contrib import admin
from .models import Film, Janr

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    filter_horizontal = ("genres",)
    list_display = ('name', 'created_by', 'approved', 'created_at')
    list_filter = ('approved', 'created_at', 'genres')
    search_fields = ('name', 'description')


    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)  # 👈 MUHIM
        

admin.site.register(Janr)

