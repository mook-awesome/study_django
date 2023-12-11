from django.urls import path, include
from watchlist_app.api.views import WatchDetailAV, WatchListAV, StreamPlatformAV

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watch-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='watch-details'),
    path('stream/', StreamPlatformAV.as_view(), name='streamplatform')
]
