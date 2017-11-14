import unittest

from handler import hello

class HandlerTest(unittest.TestCase):

  def test_event_failsWithNumberAsEvent(self):
    response = hello(1, 2)
    self.assertEqual(response.get('statusCode'), 200)
    self.assertTrue(isinstance(response.get('body'), str))
