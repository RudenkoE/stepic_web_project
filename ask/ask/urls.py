from django.conf.urls import url, include
from django.contrib import admin

from ask.views import found, not_found, init25
from qa.views import index, popular, ask, login_view, signup

urlpatterns = [

    url(r'^$', index),

    url(r'^init25/', init25),
    url(r'^login/', login_view),
    url(r'^signup/', signup),
    url(r'^ask/', ask),
    # url(r'^answer/', answer),
    url(r'^popular/', popular),
    url(r'^new/', found),

    url(r'^admin/', admin.site.urls),
    url(r'^question/', include('qa.urls')),

    url(r'^', not_found),
]
