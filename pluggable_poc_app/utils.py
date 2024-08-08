from urllib.parse import urljoin
from .waffle import should_redirect_to_commerce_coordinator_checkout
from django.conf import settings
from lms.djangoapps.commerce.utils import EcommerceService


def get_absolute_ecommerce_url(ecommerce_page_url):
    """Return the absolute URL to the ecommerce page.

    Args:
        ecommerce_page_url (str): Relative path to the ecommerce page.

    Returns:
        Absolute path to the ecommerce page.
    """
    return urljoin("localhost:18130", ecommerce_page_url)


def payment_page_url(prev_func, self):
    """Return the URL for the payment page based on the waffle switch.

    Example:
        http://localhost/enabled_service_api_path
    """
    self.dummy()
    if should_redirect_to_commerce_coordinator_checkout():
        return urljoin(
            settings.COMMERCE_COORDINATOR_URL_ROOT,
            settings.COORDINATOR_CHECKOUT_REDIRECT_PATH,
        )

    return prev_func(self)
