from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from polls.models import Poll
from django.views.generic.detail import DetailView

urlpatterns = patterns('polls.views',
    url(r'^$', 'index'),
    url(r'^(?P<poll_id>\d+)/$', 'detail', { 'name': 'Harumi' }),
    url(r'^(?P<poll_id>\d+)/results/$', 'results'),
    url(r'^(?P<poll_id>\d+)/vote/$', 'vote'),    
)


#urlpatterns = patterns('',
#       url(r'^$',
#           ListView.as_view(
#                queryset = Poll.objects.order_by('-pub_date')[:5],
#                context_object_name = 'poll_list',
#                template_name = 'polls/index.html')),
#       url(r'^(?P<pk>\d+)/$',
#           DetailView.as_view(
#                model = Poll,
#                template_name = 'polls/detail.html')),
#       url(r'^(?P<pk>\d+)/results/$',
#           DetailView.as_view(
#                model = Poll,
#                template_name = 'polls/results.html'),
#           name = 'poll_results'),
#       url(r'^(?P<pk>\d+)/vote/$', 'polls.views.vote'),
#)