"""Defines URL patterns for pizzas."""

from django.urls import path	

from . import views

urlpatterns = [
	# Home page
	path('', views.index, name='index'),

	# Show all pizzas
	path('pizzas/', views.pizzas, name='pizzas'),

	# Detail page for a single pizza
	path('pizzas/<int:pizza_id>', views.pizza, name='pizza')
]