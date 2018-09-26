from django.conf.urls import url
from qa.views import mainpg, question, popular, question_ask, question_ans, user_login, user_signup, user_logout

urlpatterns = [
	url(r'^$', mainpg, name='mainpg'),
	url(r'^question/(?P<pk>\d+)/$', question, name='question'),
	url(r'^popular/', popular, name='popular'),
	url(r'^ask/', question_ask, name='question_ask'),
	url(r'^answer/', question_ans, name='question_ans'),
	url(r'^login/', user_login, name='login'),
	url(r'^signup/', user_signup, name='signup'),
	url(r'^logout/', user_logout, name='logout'),
]
