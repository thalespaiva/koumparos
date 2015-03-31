from django.conf.urls import patterns, url


urlpatterns = patterns(
    'teacher.views',
    url(r'(\d+)/overview$', 'overview'),
    url(r'(\d+)/schedule$', 'schedule'),
)
