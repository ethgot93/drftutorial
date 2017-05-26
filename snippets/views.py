from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status

from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions

from django.contrib.auth.models import User
from snippets.serializers import UserSerializer



class SnippetList(generics.ListCreateAPIView):
	queryset = Snippet.objects.all()
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	serializer_class = SnippetSerializer

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Snippet.objects.all()
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	serializer_class = SnippetSerializer


class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer