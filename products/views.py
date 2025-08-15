from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Item
from .serializers import ItemSerializer

'''
NOTE: Conside this as a reference and follow this same coding structure or format to work on you tasks
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import DatabaseError, IntegrityError
from django.core.exceptions import ValidationError
import logging

from .models import Item
from .serializers import ItemSerializer

# Set up logging
logger = logging.getLogger(__name__)

'''
NOTE: Conside this as a reference and follow this same coding structure or format to work on you tasks
'''

# Create your views here.
class ItemView(APIView):

    def get(self, request):
            try:
                        items = Item.objects.all()
                                    serializer = ItemSerializer(items, many=True)
                                                return Response(serializer.data, status=status.HTTP_200_OK)
                                                        except DatabaseError as e:
                                                                    logger.error(f"Database error in ItemView.get: {str(e)}")
                                                                                return Response(
                                                                                                {"error": "Database error occurred while fetching items"},
                                                                                                                status=status.HTTP_500_INTERNAL_SERVER_ERROR
                                                                                                                            )
                                                                                                                                    except Exception as e:
                                                                                                                                                logger.error(f"Unexpected error in ItemView.get: {str(e)}")
                                                                                                                                                            return Response(
                                                                                                                                                                            {"error": "An unexpected error occurred"},
                                                                                                                                                                                            status=status.HTTP_500_INTERNAL_SERVER_ERROR
                                                                                                                                                                                                        )
                                                                                                                                                                                                        
                                                                                                                                                                                                            def post(self, request):
                                                                                                                                                                                                                    try:
                                                                                                                                                                                                                                serializer = ItemSerializer(data=request.data)
                                                                                                                                                                                                                                            if serializer.is_valid():
                                                                                                                                                                                                                                                            serializer.save()
                                                                                                                                                                                                                                                                            return Response(serializer.data, status=status.HTTP_201_CREATED)
                                                                                                                                                                                                                                                                                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                                                                                                                                                                                                                                                                                                except IntegrityError as e:
                                                                                                                                                                                                                                                                                                            logger.error(f"Integrity error in ItemView.post: {str(e)}")
                                                                                                                                                                                                                                                                                                                        return Response(
                                                                                                                                                                                                                                                                                                                                        {"error": "Data integrity error. Please check your input."},
                                                                                                                                                                                                                                                                                                                                                        status=status.HTTP_400_BAD_REQUEST
                                                                                                                                                                                                                                                                                                                                                                    )
                                                                                                                                                                                                                                                                                                                                                                            except ValidationError as e:
                                                                                                                                                                                                                                                                                                                                                                                        logger.error(f"Validation error in ItemView.post: {str(e)}")
                                                                                                                                                                                                                                                                                                                                                                                                    return Response(
                                                                                                                                                                                                                                                                                                                                                                                                                    {"error": "Validation error occurred", "details": str(e)},
                                                                                                                                                                                                                                                                                                                                                                                                                                    status=status.HTTP_400_BAD_REQUEST
                                                                                                                                                                                                                                                                                                                                                                                                                                                )
                                                                                                                                                                                                                                                                                                                                                                                                                                                        except DatabaseError as e:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                    logger.error(f"Database error in ItemView.post: {str(e)}")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                return Response(
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"error": "Database error occurred while saving item"},
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                status=status.HTTP_500_INTERNAL_SERVER_ERROR
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            )
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    except Exception as e:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                logger.error(f"Unexpected error in ItemView.post: {str(e)}")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            return Response(
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"error": "An unexpected error occurred"},
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            status=status.HTTP_500_INTERNAL_SERVER_ERROR
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        )    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
