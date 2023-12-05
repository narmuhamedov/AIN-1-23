from django.shortcuts import render, get_object_or_404
from .models import FilmModel, Afisha, Slider
from django.views import generic


# не полное отображение
def film_list_view(request):
    if request.method == 'GET':
        afisha_list = Afisha.objects.all()
        slider_list = Slider.objects.all()
        return render(request, template_name='films/index.html', context={
            'afisha_list': afisha_list,
            'slider_list': slider_list
        })


def primes_view(request):
    if request.method == 'GET':
        film_list = FilmModel.objects.all()
        return render(request, template_name='films/primers.html', context={
            "film_list": film_list
        })


# detail
def film_detail_view(request, id):
    if request.method == 'GET':
        film_id = get_object_or_404(FilmModel, id=id)
        return render(request, template_name='films/film_detail.html', context={'film_id': film_id})


class SearchView(generic.ListView):
    template_name = 'films/primers.html'
    context_object_name = 'film_list'
    paginate_by = 5

    def get_queryset(self):
        return FilmModel.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('id')
        return context
