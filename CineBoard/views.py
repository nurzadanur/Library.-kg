from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Avg
from .models import Movie


class MovieListView(ListView):
    model = Movie
    template_name = 'movie_list.html'
    context_object_name = 'movies'

    def get_queryset(self):
        queryset = Movie.objects.all()

        search = self.request.GET.get('q')
        if search:
            queryset = queryset.filter(title__icontains=search)

        genre = self.request.GET.get('genre')
        if genre:
            queryset = queryset.filter(genre__name=genre)

        queryset = queryset.annotate(
            avg_rating=Avg('ratings__score')
        ).order_by('-avg_rating')

        return queryset


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie_detail.html'


class MovieCreateView(CreateView):
    model = Movie
    fields = ['title', 'description', 'genre', 'release_date', 'categories']
    template_name = 'form.html'
    success_url = reverse_lazy('movie_list')


class MovieUpdateView(UpdateView):
    model = Movie
    fields = ['title', 'description', 'genre', 'release_date', 'categories']
    template_name = 'form.html'
    success_url = reverse_lazy('movie_list')


class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'delete.html'
    success_url = reverse_lazy('movie_list')