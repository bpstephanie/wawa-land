from django.test import TestCase
from .models import Event, Review
from django.contrib.auth.models import User

# Create your tests here.
class TestEventModel(TestCase):
    def setUp(self):
        self.event = Event.objects.create(
            title="Sample Event",
            slug="sample-event",
            event_about="A sample event.",
            age_range=1,
            event_location="Sample Location",
            event_date="2021-01-01",
            event_time="12:00:00",
            event_price=10.00,
        )
    
    def test_event_creation(self):
        self.assertTrue(isinstance(self.event, Event))
        self.assertEqual(self.event.__str__(), self.event.title)


class TestReviewModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.event = Event.objects.create(
            title="Sample Event",
            slug="sample-event",
            event_about="A sample event.",
            age_range=1,
            event_location="Sample Location",
            event_date="2021-01-01",
            event_time="12:00:00",
            event_price=10.00,
        )

        self.review = Review.objects.create(
            event=self.event,
            title="My Review",
            author=self.user,
            body="This event was great",
            approved=True
        )
    
    def test_review_creation(self):
        self.assertTrue(isinstance(self.review, Review))
        self.assertEqual(self.review.__str__(), f"Review {self.review.body} by {self.review.author}")