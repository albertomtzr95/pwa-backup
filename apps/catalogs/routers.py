from rest_framework import routers

from apps.catalogs.views import *

router = routers.SimpleRouter()
router.register(r'countries', CountryViewSet)
router.register(r'application-methods', ApplicationMethodViewSet)
router.register(r'business-activities', BusinessActivityViewSet)
router.register(r'cancellation-reasons', CancellationReasonViewSet)
router.register(r'cleaning', CleaningViewSet)
router.register(r'concepts', ConceptViewSet)
router.register(r'custom-descriptions', CustomDescriptionViewSet)
router.register(r'discounts', DiscountViewSet)
router.register(r'extras', ExtraViewSet)
router.register(r'indications', IndicationViewSet)
router.register(r'infestation-degrees', InfestationDegreeViewSet)
router.register(r'job-titles', JobTitleViewSet)
router.register(r'origin-sources', OriginSourceViewSet)
router.register(r'payment-methods', PaymentWayViewSet)
router.register(r'payment-ways', PaymentWayViewSet)
router.register(r'plague-categories', PlagueCategoryViewSet)
router.register(r'plagues', PlagueViewSet)
router.register(r'product-presentations', PresentationViewSet)
router.register(r'service-types', ServiceTypeViewSet)
router.register(r'rejection-reasons', RejectionReasonViewSet)
router.register(r'taxes', TaxViewSet)
router.register(r'product-types', TypeProductViewSet)
router.register(r'product-units', UnitProductViewSet)
router.register(r'vouchers', VoucherViewSet)

urlpatterns = router.urls
