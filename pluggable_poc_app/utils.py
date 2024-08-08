from urllib.parse import urljoin
from .waffle import should_redirect_to_commerce_coordinator_checkout
from django.conf import settings

def payment_page_url(prev_func, self):
    """Return the URL for the payment page based on the waffle switch.

    Example:
        http://localhost/enabled_service_api_path
    """
    if should_redirect_to_commerce_coordinator_checkout():
        return urljoin(
            settings.COMMERCE_COORDINATOR_URL_ROOT,
            settings.COORDINATOR_CHECKOUT_REDIRECT_PATH,
        )

    return prev_func(self)
