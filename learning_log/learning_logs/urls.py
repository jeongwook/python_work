"""Define URL patterns for learning_logs."""

from django.urls import path

from . import views

    # 1. Add an import:  from my_app import views
    # 2. Add a URL to urlpatterns:  path('', views.home, name='home')

urlpatterns = [
	# Home page
	path('', views.index, name='index'),

	#Show all topics.
	path('topics/', views.topics, name='topics'),

	# Detail page for a single topic
	path('topics/<int:topic_id>/', views.topic, name='topic')
]