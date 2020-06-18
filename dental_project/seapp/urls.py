from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import WorkTimesViewSet,VisitViewSet, ReservationView , makeReservation
from django.conf.urls import url

router = DefaultRouter()
router.register('worktimes',WorkTimesViewSet)
router.register('visit',VisitViewSet)

urlpatterns = [
    url(r'^reserve/', ReservationView.as_view() ),
    url(r'^make-reserve/', makeReservation.as_view() ),
]

urlpatterns+=router.urls