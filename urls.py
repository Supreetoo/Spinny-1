from django.urls import path
from .views import BoxCreateView, BoxDeleteView, BoxUpdateView, ListBoxesView, ListMyBoxesView

urlpatterns = [
    path('box/', BoxCreateView.as_view(), name='create-box'),
    path('box/<int:pk>/', BoxUpdateView.as_view(), name='update-box'),
    path('list-boxes/', ListBoxesView.as_view(), name='list-boxes'),
    path('listMyboxes/', ListMyBoxesView.as_view(), name='listmyboxes'),
    path('Deletebox/', BoxDeleteView.as_view(), name='listmyboxes'),
    

    # ... other URL patterns ...
]
