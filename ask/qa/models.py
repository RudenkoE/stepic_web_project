from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    def new():
        return self.order_by('-id')
    def popular():
        popular_list = self.all()[:]
	sort = sorted(popular_list, key=lambda question: question.likes.count(), 			      reverse=True
		)
	return self.order_by('-rating')

class Question(models.Model):
	"""docstring for Question"""
	title = models.CharField(max_length=200)
	text = models.TextField()
	added_at = models.DateField(blank=True, auto_now_add=True)
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User, default='x')
	likes = models.ManyToManyField(User, related_name='likes')
	objects = QuestionManager()

	def get_answers(self):
		return self.answer_set.all()
		
	def get_absolute_url(self):
		return reverse('question', args=[str(self.id)])

		
class Answer(models.Model):
	"""docstring for Question"""
	text = models.TextField()
	added_at = models.DateField(blank=True, auto_now_add=True)
	rating = models.IntegerField(default=0)
	question = models.ForeignKey(Question)
	author = models.ForeignKey(User)


class Session(models.Model):
	"""docstring for Session"""
	key = models.CharField(max_length=100, unique=True)
	user = models.ForeignKey(User)
	expires = models.DateTimeField(blank=True)
