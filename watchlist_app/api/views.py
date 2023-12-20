from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework import generics, mixins, viewsets
from watchlist_app.models import WatchList, StreamPlatform, Review
from watchlist_app.api.serializers import (WatchListSerializer, StreamPlatformSerializer, ReviewSerializer)
from rest_framework import status
from django.shortcuts import get_object_or_404

### Classs based views ##############################################
class StreamPlatformMVS(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer

class StreamPlatformVS(viewsets.ViewSet):
    def list(self, request):
        queryset = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = StreamPlatform.objects.all()
        watchilst = get_object_or_404(queryset, pk=pk)
        serializer = StreamPlatformSerializer(watchilst)
        return Response(serializer.data)

    def create(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, reqeuest, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    def get_queryset(self):
        return Review.objects.all()
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        watchlist = WatchList.objects.get(pk=pk)
        review_user = self.request.user
        review_queryset = Review.objects.filter(watchlist=watchlist, review_user=review_user)
        if review_queryset.exists():
            raise ValidationError('You have already reviewed this watchlist')
        serializer.save(watchlist=watchlist, review_user=review_user)
    
class ReviewList(generics.ListCreateAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = Review.objects.all()
        serializer_class = ReviewSerializer

class StreamPlatformAV(APIView):
    
    def get(self, request):
       platform = StreamPlatform.objects.all()
       serializer = StreamPlatformSerializer(platform, many=True) 
       return Response(serializer.data)
   
    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StreamPlatformDetailAV(APIView):
    
    def get(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
            serializer = StreamPlatformSerializer(platform)
            return Response(serializer.data)
        except StreamPlatform.DoesNotExist:
            return Response({'ERROR': 'platform does not exist'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class WatchListAV(APIView):
    
    def get(self, request):
        watchList = WatchList.objects.all()
        serializer = WatchListSerializer(watchList, many=True) # 여러개를 serialize하려면 'many=True'가 필요하다.
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class WatchDetailAV(APIView):

    def get(self, request, pk):
        try:
            watchList = WatchList.objects.get(pk=pk)
            serializer = WatchListSerializer(watchList)
            return Response(serializer.data)
        except WatchList.DoesNotExist:
            return Response({'ERROR': 'watchList does not exist'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        watchList = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(watchList, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, reqeuest, pk):
        watchList = WatchList.objects.get(pk=pk)
        watchList.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
### Function based views ##############################################
# @api_view(['GET', 'POST'])
# def movie_list(request):
    
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True) # 여러개를 serialize하려면 'many=True'가 필요하다.
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else: 
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_details(request, pk):
    
#     if request.method == 'GET':
#         try:
#             movie = Movie.objects.get(pk=pk)
#             serializer = MovieSerializer(movie)
#             return Response(serializer.data)
#         except Movie.DoesNotExist:
#             return Response({'ERROR': 'Movie does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
#     if request.method =='PUT':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)        
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)