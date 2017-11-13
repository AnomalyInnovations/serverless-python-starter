import unittest

from handler import hello

class HandlerTest(unittest.TestCase):

    def test_event_failsWithNumberAsEvent(self):
        self.assertFalse(False, msg="hello: function succeeded with event as Number")
