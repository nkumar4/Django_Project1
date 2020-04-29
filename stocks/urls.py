

from django.urls import path
from . import views

urlpatterns = [
    path('stocks.html', views.stocks, name="stocks"),
    #path('delete/<list_id>', views.delete, name="delete"),
    #path('crossed/<list_id>', views.crossed, name="crossed"),
    #path('uncrossed/<list_id>', views.uncrossed, name="uncrossed"),
    #path('edit/<list_id>', views.edit, name="edit"),
]
