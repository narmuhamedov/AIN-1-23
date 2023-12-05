from django.urls import path
from .views import film_list_view, film_detail_view, primes_view, SearchView

urlpatterns = [
    path('', film_list_view),
    path('premiers/', primes_view),
    path('film_list/<int:id>/', film_detail_view),
    path('search/', SearchView.as_view(), name='search')
]