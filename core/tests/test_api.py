from unittest import mock

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.test import Client

from core.models import Task


class TaskViewSetTestCase(APITestCase):
    def setUp(self):
        self.client = Client()
        self.task = Task.objects.create(url='www.google.com',
                                        identifier='AG7Ne0pm',
                                        analyzed_data={
                                            "head": {"count": 1, "nested": 9},
                                            "body": {"count": 1, "nested": 74}
                                        })

    def test_post(self):
        with mock.patch('core.serializers.get_random_string', return_value='BGcN10pt'):
            url = reverse('create_task')
            data = {"url": "www.google.com"}
            response = self.client.post(url, data=data)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual('BGcN10pt', response.data["identifier"])

    def test_get(self):
        url = reverse('result', kwargs={'identifier': 'AG7Ne0pm'})
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(
            {"head": {"count": 1, "nested": 9},
             "body": {"count": 1, "nested": 74}},
            response.data)
