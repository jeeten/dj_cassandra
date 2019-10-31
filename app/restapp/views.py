from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Article

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, ArticleSerializer

# from tutorial.quickstart.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ArticleView(APIView):
    def get(self, request):
        print(dir(request))
        print(request.query_params)
        articles = Article.objects.all()
        serializer = ArticleSerializer( articles, many=True )
        return Response({"articles": serializer.data})

    def post(self, request) :
        article = request.data.get( 'article' )

        # Create an article from the above data
        serializer = ArticleSerializer( data=article )
        if serializer.is_valid( raise_exception=True ) :
            article_saved = serializer.save()
        return Response( {"success" : "Article '{}' created successfully".format( article_saved.title )} )

