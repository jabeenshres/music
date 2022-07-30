from django.shortcuts import render
from django.urls import reverse_lazy, reverse

from django.views.generic import (
      CreateView,
      UpdateView,
      ListView,
      DeleteView
)
from .models import Album, Song
from .forms import AlbumForm, SongFormset


class AlbumCreateView(CreateView):
    template_name = "createupdate_freshhousesales.html"
    form_class = AlbumForm
    success_url = reverse_lazy('album:create')
    success_message = 'Album has been successfully created.'
#     view_data_url = "freshhousesales:list"
    heading = 'Album'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

      #   if self.view_data_url:
      #       context['view_data'] = self.view_data_url
        if self.heading:
            context['heading'] = self.heading
        if self.request.method == "POST":
            context['formset'] = SongFormset(self.request.POST)
        else:
            context['formset'] = SongFormset()
        
        return context

    def form_valid(self, form, *args, **kwargs):
        context = self.get_context_data()
        item_details = context['formset']

        with transaction.atomic():
            if item_details.is_valid():
                self.object = form.save(commit=False)
                new_date = datetime.now()
                self.object.date = datetime(
                    self.object.date.year,
                    self.object.date.month,
                    self.object.date.day,
                    new_date.hour,
                    new_date.minute,
                    new_date.second,
                    new_date.microsecond
                )
                self.object.save()
                item_details.instance = self.object
                item_details.save()
            else:
                return super().form_invalid(form)

        return super().form_valid(form)
