import unittest
from info import get_ip_info
class TestGetIpInfo(unittest.TestCase):
    def test_get_ip_info_with_domain(self):
        info = get_ip_info("google.com")
        self.assertIsNotNone(info)

    def test_get_ip_info_with_ip(self):
        info = get_ip_info("8.8.8.8")
        self.assertIsNotNone(info)
