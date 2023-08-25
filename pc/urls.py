from django.urls import path
from .api_views import PCListCreateAPIView, PCDetailAPIView

urlpatterns = [
    path("api/pcs/", PCListCreateAPIView.as_view(), name="pc-list"),
    path("api/pcs/<int:pk>/", PCDetailAPIView.as_view(), name="pc-detail"),
]
