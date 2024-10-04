from django.urls import path

from .views import meetings_view
urlpatterns = [path('', meetings_view, name='meetings_home')]