from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('courses', views.CourseView)

urlpatterns = [
    path('courses.html', include(router.urls)),
    # path('portfolio.html', views.portfolio, name="portfolio"),
    # path('deletestock/<id>', views.deletestock, name="deletestock"),
    #path('crossed/<list_id>', views.crossed, name="crossed"),
    #path('uncrossed/<list_id>', views.uncrossed, name="uncrossed"),
    #path('edit/<list_id>', views.edit, name="edit"),
]
