from django.conf.urls import patterns, url


urlpatterns = patterns(
    'teacher.views',
    url(r'(\d+)/overview/(\w{4})?$', 'overview'),
    url(r'(\d+)/schedule$', 'schedule'),
    url(r'(\d+)/dashboard$', 'dashboard'),
)
