from django import forms
from .models import Film, Janr

class FilmForm(forms.ModelForm):
    genres = forms.ModelMultipleChoiceField(
        queryset=Janr.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Janrlar"
    )

    # Foydalanuvchi anonim qo'shishi uchun checkbox
    anonymous = forms.BooleanField(
        required=False,
        label="Anonym qo‘shish (foydalanuvchi nomi yashirin bo‘ladi)"
    )

    class Meta:
        model = Film
        fields = ['name', 'description', 'duration', 'direct_by', 'actor', 'image', 'genres']
