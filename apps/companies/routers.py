from rest_framework import routers

from apps.companies.views import CompanyViewSet

router = routers.SimpleRouter()
router.register(r'companies', CompanyViewSet)

urlpatterns = router.urls
