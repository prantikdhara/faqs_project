from django.db import models

# Create your models here.

from ckeditor.fields import RichTextField

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True, null=True)
    answer_hi = RichTextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)
    answer_bn = RichTextField(blank=True, null=True)

    def get_translation(self, lang='en'):
        if lang == 'hi':
            return {'question': self.question_hi or self.question, 'answer': self.answer_hi or self.answer}
        elif lang == 'bn':
            return {'question': self.question_bn or self.question, 'answer': self.answer_bn or self.answer}
        return {'question': self.question, 'answer': self.answer}
