from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Box
from .serializers import BoxListSerializer, BoxSerializer
from django.contrib.auth.decorators import login_required


class BoxCreateView(APIView):
    def post(self, request):
        if not request.user.is_authenticated:
            return Response({"message": "You must be logged in to add a box."}, status=status.HTTP_403_FORBIDDEN)

        serializer = BoxSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BoxUpdateView(APIView):
    def put(self, request, pk):
        if not request.user.is_staff:
            return Response({"message": "Only staff users can update box."}, status=status.HTTP_403_FORBIDDEN)

        box = Box.objects.get(pk=pk)
        serializer = BoxSerializer(box, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ListBoxesView(APIView):
    def get(self, request):
        boxes = Box.objects.all()

        length_more_than = request.query_params.get('length_more_than')
        length_less_than = request.query_params.get('length_less_than')
        breadth_more_than = request.query_params.get('breadth_more_than')
        breadth_less_than = request.query_params.get('breadth_less_than')
        height_more_than = request.query_params.get('height_more_than')
        height_less_than = request.query_params.get('height_less_than')
        area_more_than = request.query_params.get('area_more_than')
        area_less_than = request.query_params.get('area_less_than')
        volume_more_than = request.query_params.get('volume_more_than')
        volume_less_than = request.query_params.get('volume_less_than')
        created_by = request.query_params.get('created_by')
        created_before = request.query_params.get('created_before')
        created_after = request.query_params.get('created_after')

        if length_more_than:
            boxes = boxes.filter(length__gt=float(length_more_than))
        if length_less_than:
            boxes = boxes.filter(length__lt=float(length_less_than))
        if breadth_more_than:
            boxes = boxes.filter(width__gt=float(breadth_more_than))
        if breadth_less_than:
            boxes = boxes.filter(width__lt=float(breadth_less_than))
        if height_more_than:
            boxes = boxes.filter(height__gt=float(height_more_than))
        if height_less_than:
            boxes = boxes.filter(height__lt=float(height_less_than))
        if area_more_than:
            boxes = boxes.filter(length__gt=float(area_more_than)) | \
                    boxes.filter(width__gt=float(area_more_than)) | \
                    boxes.filter(height__gt=float(area_more_than))
        if area_less_than:
            boxes = boxes.filter(length__lt=float(area_less_than)) | \
                    boxes.filter(width__lt=float(area_less_than)) | \
                    boxes.filter(height__lt=float(area_less_than))
        if volume_more_than:
            boxes = boxes.filter(length__gt=float(volume_more_than)) | \
                    boxes.filter(width__gt=float(volume_more_than)) | \
                    boxes.filter(height__gt=float(volume_more_than))
        if volume_less_than:
            boxes = boxes.filter(length__lt=float(volume_less_than)) | \
                    boxes.filter(width__lt=float(volume_less_than)) | \
                    boxes.filter(height__lt=float(volume_less_than))
        if created_by:
            boxes = boxes.filter(creator__username=created_by)
        if created_before:
            boxes = boxes.filter(created_at__lt=created_before)
        if created_after:
            boxes = boxes.filter(created_at__gt=created_after)

        serializer = BoxListSerializer(boxes, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ListMyBoxesView(APIView):
    @login_required
    def get(self, request, *args, **kwargs):
        boxes = Box.objects.filter(creator=request.user)

        length_more_than = request.query_params.get('length_more_than')
        length_less_than = request.query_params.get('length_less_than')
        breadth_more_than = request.query_params.get('breadth_more_than')
        breadth_less_than = request.query_params.get('breadth_less_than')
        height_more_than = request.query_params.get('height_more_than')
        height_less_than = request.query_params.get('height_less_than')
        area_more_than = request.query_params.get('area_more_than')
        area_less_than = request.query_params.get('area_less_than')
        volume_more_than = request.query_params.get('volume_more_than')
        volume_less_than = request.query_params.get('volume_less_than')

        if length_more_than:
            boxes = boxes.filter(length__gt=float(length_more_than))
        if length_less_than:
            boxes = boxes.filter(length__lt=float(length_less_than))
        if breadth_more_than:
            boxes = boxes.filter(width__gt=float(breadth_more_than))
        if breadth_less_than:
            boxes = boxes.filter(width__lt=float(breadth_less_than))
        if height_more_than:
            boxes = boxes.filter(height__gt=float(height_more_than))
        if height_less_than:
            boxes = boxes.filter(height__lt=float(height_less_than))
        if area_more_than:
            boxes = boxes.filter(length__gt=float(area_more_than)) | \
                    boxes.filter(width__gt=float(area_more_than)) | \
                    boxes.filter(height__gt=float(area_more_than))
        if area_less_than:
            boxes = boxes.filter(length__lt=float(area_less_than)) | \
                    boxes.filter(width__lt=float(area_less_than)) | \
                    boxes.filter(height__lt=float(area_less_than))
        if volume_more_than:
            boxes = boxes.filter(length__gt=float(volume_more_than)) | \
                    boxes.filter(width__gt=float(volume_more_than)) | \
                    boxes.filter(height__gt=float(volume_more_than))
        if volume_less_than:
            boxes = boxes.filter(length__lt=float(volume_less_than)) | \
                    boxes.filter(width__lt=float(volume_less_than)) | \
                    boxes.filter(height__lt=float(volume_less_than))

        serializer = BoxListSerializer(boxes, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
class BoxDeleteView(APIView):
    def delete(self, request, box_id):
        try:
            box = Box.objects.get(pk=box_id)
        except Box.DoesNotExist:
            return Response({"error": "Box not found"}, status=status.HTTP_404_NOT_FOUND)
        
        box.delete()
        return Response({"message": "Box deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        
