from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from snippets import views


user_list = views.UserViewSet.as_view({
	'get': 'list'
	})

user_detail = views.UserViewSet.as_view({
	'get': 'retrieve'
	})


# API Endpoints
urlpatterns = [
	url(r'^$', views.api_root),
	url(r'^snippets/$', 
		views.SnippetList.as_view(),
		name='snippet-list'),
	url(r'^snippets/(?P<pk>[0-9]+)/$', 
		views.SnippetDetail.as_view(),
		name='snippet-detail'),
	url(r'^users/$', 
		user_list,
		name='user-list'),
	url(r'^users/(?P<pk>[0-9]+)/$', 
		user_detail,
		name='user-detail'),
]


urlpatterns = format_suffix_patterns(urlpatterns)