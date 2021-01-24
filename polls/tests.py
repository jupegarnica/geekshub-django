from django.test import TestCase
from .models import Question, ChoiceNumber

class ChoiceTestCase(TestCase):
    def setUp(self):
        question = Question.objects.create(question_text="How much is 1+1?")
        ChoiceNumber.objects.create(question=question,choice_number=1)
        ChoiceNumber.objects.create(question=question,choice_number=2)
        ChoiceNumber.objects.create(question=question,choice_number=3)
    
    def test_questions_max_choice(self):
        questions_query = Question.objects.all()

        for question in questions_query.iterator():
            num_choices = len(ChoiceNumber.objects.all())
            self.assertLess(num_choices,4)


