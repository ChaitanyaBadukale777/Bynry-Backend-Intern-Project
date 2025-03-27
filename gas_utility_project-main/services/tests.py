from django.test import TestCase
from .models import ServiceRequest
from django.utils import timezone

class ServiceRequestModelTest(TestCase):

    def setUp(self):
        """Set up a sample service request before each test"""
        self.service_request = ServiceRequest.objects.create(
            email="test@example.com",
            customer_name="John Doe",
            status="Pending"
        )

    def test_service_request_creation(self):
        """Test if the service request is created successfully"""
        self.assertEqual(self.service_request.email, "test@example.com")
        self.assertEqual(self.service_request.customer_name, "John Doe")
        self.assertEqual(self.service_request.status, "Pending")
        self.assertIsNotNone(self.service_request.created_at)

    def test_service_request_update(self):
        """Test updating the status of a service request"""
        self.service_request.status = "Completed"
        self.service_request.save()
        updated_request = ServiceRequest.objects.get(id=self.service_request.id)
        self.assertEqual(updated_request.status, "Completed")

    def test_created_at_auto_now_add(self):
        """Ensure created_at is automatically set"""
        self.assertIsNotNone(self.service_request.created_at)
        self.assertLessEqual(self.service_request.created_at, timezone.now())

    def test_updated_at_auto_now(self):
        """Ensure updated_at changes when saving"""
        old_updated_at = self.service_request.updated_at
        self.service_request.status = "In Progress"
        self.service_request.save()
        self.assertNotEqual(old_updated_at, self.service_request.updated_at)

    def test_string_representation(self):
        """Test the model's __str__ method (if applicable)"""
        expected_str = f"{self.service_request.customer_name} - {self.service_request.status}"
        self.assertEqual(str(self.service_request), expected_str)
