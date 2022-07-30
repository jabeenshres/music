from django import forms
from django.forms.models import inlineformset_factory

from .models import Album, Song



class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = "__all__"
        widgets = {
            "released_date": forms.DateInput(attrs={'type': 'date'})
        }
    
class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        exclude = ("related_object", )


SongFormset = inlineformset_factory(
    Album,
    Song,
    form=SongForm,
    extra=1,
) 