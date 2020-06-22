from django.test import TestCase
from django.utils import timezone
import datetime
from .models import Visit


class QuestionModelTests(TestCase):

    def test_was_reserved(self):

        future_question = Visit(time = timezone.now() + datetime.timedelta(days=30))
        self.assertIs(future_question.reserved, True)

# Create your tests here.

