"""
TestAdmin

"""

import app
import json
import unittest

from nose.tools import assert_equal, assert_not_equal


class TestAdmin(unittest.TestCase):
    """
    Test admin functionality

    """

    def setUp(self):
        """
        Setup to run before any tests are run

        """
        self.app = app.app.test_client()

    def tearDown(self):
        """
        Run after tests are done

        """

    def test_get_slides(self):
        response = self.app.get('/admin/get/slides')
        json_data = json.loads(response.data.decode("utf-8"))
        assert_equal(True, 'slides' in json_data)
