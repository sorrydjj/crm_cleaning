from django.urls import path

from api.views import (get_token_view,
                       ApiClientCreateView,
                       ApiFineCreateView,
                       ApiBonusCreateView,
                       ApiInventoryCreateView,
                       ApiObjectTypeCreateView,
                       ApiServiceOrderUpdateView,
                       ApiServiceOrderDeleteView, ApiInventoryOrderDeleteView, Calendar, ApiServiceCreateView)

app_name = 'api'

urlpatterns = [
    path('get-csrf-token/', get_token_view),
    path("client/create/", ApiClientCreateView.as_view(), name='client_create'),
    path('fine/create/', ApiFineCreateView.as_view()),
    path('bonus/create/', ApiBonusCreateView.as_view()),
    path('inventory/create/', ApiInventoryCreateView.as_view()),
    path('object_type/create/', ApiObjectTypeCreateView.as_view()),
    path('service/create/', ApiServiceCreateView.as_view()),
    path('order/update/service/<int:pk>/', ApiServiceOrderUpdateView.as_view(), name='service_order_update'),
    path('order/delete/service/<int:pk>/', ApiServiceOrderDeleteView.as_view(), name='service_order_delete'),
    path('delete/inventory/<int:pk>/', ApiInventoryOrderDeleteView.as_view(), name='inventory_order_delete'),
    path('order/list/', Calendar.as_view())
]
