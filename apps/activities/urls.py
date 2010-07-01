from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^home/$', 'activities.views.home', name="activity_home"),
    url(r'^(?P<item_type>activity|commitment|goal)_list/$', 'activities.views.list', name="activity_list"),
    
    # Actions
    url(r'^like_(?P<item_type>activity|commitment|goal)/(?P<item_id>\d+)/$', 
      'activities.views.like', name='activity_like'),
    url(r'^unlike_(?P<item_type>activity|commitment|goal)/(?P<item_id>\d+)/$', 
      'activities.views.unlike', name='activity_unlike'),
    url(r'^add_(?P<item_type>activity|commitment|goal)/(?P<item_id>\d+)/$',
      'activities.views.add_participation', name='add_participation'),
    url(r'^remove_(?P<item_type>activity|commitment|goal)/(?P<item_id>\d+)/$',
      'activities.views.remove_participation', name='remove_participation'),
    url(r'^request_(?P<item_type>activity|commitment|goal)_points/(?P<item_id>\d+)/$',
      'activities.views.request_points', name='request_points'),
    url(r'^view_codes/(?P<activity_id>\d+)/$', 'activities.views.view_codes', name='view_codes')
)