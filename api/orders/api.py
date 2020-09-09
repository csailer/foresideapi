from rest_framework import routers
from . import views as order_views

router = routers.DefaultRouter()
router.register(r'orders', order_views.OrderViewset)
router.register(r'orderstatus', order_views.OrderStatusViewset)
