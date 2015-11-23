from django.conf.urls import include, url, patterns
from apps.gold import views

urlpatterns = patterns ('',
  url(r'^$', views.index, name='index'),
  url(r'^process$', views.process_gold, name='process'),
  url(r'^rest$', views.reset, name='reset')
  )


