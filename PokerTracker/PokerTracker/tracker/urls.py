from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('sessions/', views.SessionListView.as_view(), name='sessions'),
    path('session/<int:pk>', views.SessionDetailView.as_view(), name='session-detail'),
    path('place/create/', views.PlaceCreate.as_view(), name='place_create'),
    path('place/<int:pk>', views.PlaceDetailView.as_view(), name='place-detail'),
    path('game/create/', views.GameCreate.as_view(), name='game_create'),
    path('game/<int:pk>', views.GameDetailView.as_view(), name='game-detail'),
    path('session/create/', views.SessionCreate.as_view(), name='session_create'),
    path('session/<int:pk>/update/', views.SessionUpdate.as_view(), name='session_update'),
    path('session/<int:pk>/delete/', views.SessionDelete.as_view(), name='session_delete'),
    path('session/edit/', views.edit_session, name='edit_session'),
]
