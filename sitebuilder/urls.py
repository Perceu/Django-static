from django.urls import path
from sitebuilder.views import page


urlpatterns = (
    path('<slug:slug>', page, name='page'),
    path('', page, name='homepage'),
)