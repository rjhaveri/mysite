from django.utils import unittest, timezone
from polls.models import Poll

class PollTestCase(unittest.TestCase):
    def setUp(self):
        self.poll = Poll.objects.create(question="What's new?", pub_date=timezone.now())

    def test_poll_question(self):
        """Poll got the question right"""
        self.assertEqual(self.poll.question, 'What\'s new?')
 