from django.urls import path,include

from .views import ReviewSearchView

urlpatterns=[
    path('searchReview',ReviewSearchView.as_view())
]