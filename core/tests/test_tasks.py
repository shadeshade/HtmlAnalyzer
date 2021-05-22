from unittest.mock import patch

from django.test import Client
from django.test import TestCase

from core.models import Task
from core.tasks import analyze_html


class AnalyzeHtmlTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.task = Task.objects.create(id=1,
                                        url='www.example.com',
                                        identifier='AG7Ne0pm',
                                        analyzed_data={})

    def test_save_to_db(self):
        with patch('core.tasks.get_url') as mocked_get_url:
            mocked_get_url.return_value.content = """
            <html>
              <head>
                <title>Href Attribute Example</title>
              </head>
              <body>
                <h1>Href Attribute Example</h1>
                <p>
                  <a href="https://www.example.com/"> Page</a>
                </p>
              </body>
            </html>"""

            analyze_html(self.task.id)
            self.task.refresh_from_db()

            self.assertEqual({
                "html": {"count": 1, "nested": 6},
                "head": {"count": 1, "nested": 1},
                "title": {"count": 1, "nested": 0},
                "a": {"count": 1, "nested": 0},
                "body": {"count": 1, "nested": 3},
                "p": {"count": 1, "nested": 1},
                "h1": {"count": 1, "nested": 0},
            },
                self.task.analyzed_data)
