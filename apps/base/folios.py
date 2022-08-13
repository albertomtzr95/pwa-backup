from apps.companies.models import Company


def company():
    last_company = Company.objects.order_by('-created_at').first()
    if not last_company:
        return 'PWA-1'
    last_folio = int(last_company.folio.split('-')[1])
    last_folio += 1
    return f'PWA-{last_folio}'
