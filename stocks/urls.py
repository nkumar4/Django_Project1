

from django.urls import path
from . import views

urlpatterns = [
    path('stocks.html', views.stocks, name="stocks"),
    path('portfolio.html', views.portfolio, name="portfolio"),
    path('deletestock/<id>', views.deletestock, name="deletestock"),
    #path('crossed/<list_id>', views.crossed, name="crossed"),
    #path('uncrossed/<list_id>', views.uncrossed, name="uncrossed"),
    #path('edit/<list_id>', views.edit, name="edit"),
]
