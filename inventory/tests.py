from django.test import TestCase
from inventory.models import Vendor


class VendorMethodTests(TestCase):

    def test_vendor_with_empty_name(self):
        vendor = Vendor.objects.get(id=1)
        self.assertNotEqual(vendor.name, None)