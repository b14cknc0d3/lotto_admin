from dynamic_rest import routers
from . import views
from django.urls import path, include

router = routers.DynamicRouter()
router.register(r'search/one', views.OneLSearchViewSet)
router.register(r'search/two', views.TwoLSearchViewSet)
router.register(r'search/five', views.FiveLSearchViewSet)
router.register(r'two', views.TwoLViewSet)
router.register(r'five', views.FiveLViewSet)
router.register(r'reseller', views.UserViewSet)
router.register(r'one', views.OneLViewSet)
urlpatterns = [
    path('api/saledatas/', include(router.urls))
]
