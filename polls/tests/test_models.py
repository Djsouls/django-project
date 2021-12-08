from django.test import TestCase
from django.utils import timezone


from polls.models import Question, Choice

class QuestionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Question.objects.create(
            question_text='Who is there?',
            pub_date=timezone.now()
        )

    def test_question_properly_created(self):
        question = Question.objects.get(id=1)

        self.assertEquals(question.question_text, 'Who is there?')

    def test_question_string_representation_is_question_text(self):
        question = Question.objects.get(id=1)

        self.assertEquals(question.question_text, str(question))

class ChoiceModelTest(TestCase):
    CHOICES = ['Nothing..', 'A nice cup of coffee', 'Elefants']

    @classmethod
    def setUpTestData(cls):
        q = Question.objects.create(
                question_text='What is greater than my love for you?',
                pub_date=timezone.now()
            )

        for choice in cls.CHOICES:
            q.choice_set.create(choice_text=choice, votes=0)

    def test_choice_properly_created(self):
        question = Question.objects.get(id=1)
        choices = question.choice_set.all().order_by('id')

        for i in range(choices.count()):
            self.assertEquals(choices[i].choice_text, self.CHOICES[i])
            self.assertEquals(choices[i].id, i + 1)

    def test_choices_strings_representation_are_choices_text(self):
        choices = Choice.objects.all()

        for choice in choices:
            self.assertEqual(choice.choice_text, str(choice))

    def test_number_of_choices_are_created_for_question(self):
        question = Question.objects.get(id=1)

        self.assertEquals(len(self.CHOICES), question.choice_set.count())
