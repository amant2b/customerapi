from rest_framework import routers
from . import views

router= routers.DefaultRouter()

router.register('', views.customerApi)


urlpatterns = router.urls