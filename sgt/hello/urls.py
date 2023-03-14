from django.urls import path
from . import views

urlpatterns = [
	# path("", views.index, name="index"),
	#path("", views.greet, name="greet")
    path("<str:nome>", views.greet, name="greet")
	
	
]
