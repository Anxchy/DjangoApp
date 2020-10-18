from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import get_object_or_404


#modelViewSet 
'''very simple to do all methods just using 2 line of code'''
class modelViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()  


#genericviewset

class genercicViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,
                    mixins.CreateModelMixin,mixins.RetrieveModelMixin, 
                        mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()



#viewset and routers
class ArticleViewSet(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def list(self, request):
        articleData=Article.objects.all()
        serializer=ArticleSerializer(articleData, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

    def retrieve(self, request, pk=None):
        querySet = Article.objects.all()
        article = get_object_or_404(querySet, pk=pk)
        serializer=ArticleSerializer(article)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        articleData = Article.objects.get(pk=pk)
        serializer=ArticleSerializer(articleData, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        articleData = Article.objects.get(pk=pk)
        articleData.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




#classbased generic view
class GenericApiList(generics.GenericAPIView, mixins.ListModelMixin,
                    mixins.CreateModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    #authentication_classes = [SessionAuthentication, BasicAuthentication] '''for basic authentication'''
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    #we can write our generic api detail in this class by using lookup_field=id
    #and then get pass id in method as none if id then retrieve else get list .


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

#classbased generic view
class GenericApiDetail(generics.GenericAPIView, mixins.RetrieveModelMixin, 
                        mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)







#class based view
class ArticleList(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        articleData=Article.objects.all()
        serializer=ArticleSerializer(articleData, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

#class based view
class Articledetail(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get_object(self, id):
        try:
            return Article.objects.get(pk=id)
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        articleData = self.get_object(id)
        serializer = ArticleSerializer(articleData)
        return Response(serializer.data)
    
    def put(self, request, id):
        articleData = self.get_object(id)
        serializer=ArticleSerializer(articleData, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        articleData = self.get_object(id)
        articleData.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




#function based view
@api_view(['GET','POST'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def article_list(request):
    if request.method == 'GET':
        articleData=Article.objects.all()
        serializer=ArticleSerializer(articleData, many=True)
        #dic={'kul':'hjkhhjhk'} testing
        return Response(serializer.data)

    
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#function based view
#customized authentications session based and basic authentication
@api_view(['GET','PUT','DELETE'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def article_detail(request, pk):
    try:
        articleData = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ArticleSerializer(articleData)
        return Response(serializer.data)

    elif request.method == 'PUT':
        #we dnt need to write below code explicitly to parse as we are using api_view decorator and request.data
        #data = JSONParser().parse(request)
        serializer=ArticleSerializer(articleData, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        articleData.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



