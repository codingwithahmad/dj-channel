from django.urls import path
from .views import index, echo_image


urlpatterns = [
	path('', index, name='index'),
	path('image/', echo_image, name='echo_image')
] 
