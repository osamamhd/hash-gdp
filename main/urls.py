from django.urls import path
from . import views
urlpatterns = [
    path('boats/', views.BoatListView.as_view()),
    path('boats/<int:pk>/', views.BoatDetailView.as_view()),
    path('boats_owner/', views.BoatOwnerListView.as_view()),
    path('boats_owner/<int:pk>/<slug:boat_owner_slug>/', views.BoatOwnerDetailView.as_view()),
    path('loads/', views.LoadListView.as_view()),
    path('loads/<int:pk>/', views.LoadDetailView.as_view()),
    path('tilapia_quantity/', views.tilapia_quantity),
    path('mackerel_quantity/', views.mackerel_quantity),
    path('grouper_quantity/', views.grouper_quantity),
    path('agents/', views.AgentListView.as_view()),
    path('orders/', views.OrderListView.as_view()),
    path('orderloads/', views.OrderLoadListView.as_view()),
    path('orderloads/pending/', views.PendingOrderLoad.as_view()),
    path('orderloads/done/', views.DoneOrderLoad.as_view()),
    path('orderloads/<int:pk>/', views.OrderLoadDetailView.as_view()),

    path('tilapia_requested/', views.tilapia_requested),
    path('mackerel_requested/', views.mackerel_requested),
    path('grouper_requested/', views.grouper_requested),

    path('tilapia_delivered/', views.tilapia_delivered),
    path('mackerel_delivered/', views.mackerel_delivered),
    path('grouper_delivered/', views.grouper_delivered),
]