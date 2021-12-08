from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from polls.models import Question, Choice

class QuestionListViewTest(TestCase):
    @classmethod
    def setUpData(cls):
        questions_n = 10

        for i in range(questions_n):
            Question.create(
                question_text = f'Question  {i+1}',
                pub_date = timezone.now()
            )

    def test_index_accessible_by_name_returns_200(self):
        response = self.client.get(reverse('polls:index'))

        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('polls:index'))
        
        self.assertEquals(response.status_code, 200)

        self.assertTemplateUsed(response, 'polls/index.html')
