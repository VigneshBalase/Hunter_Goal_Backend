from django.shortcuts import render
# Create your views here.
import logging
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Enquiry, CollegeEnquiry, InstructorEnquiry, SummaryEnquiry, InternshipEnquiry
from .serializers import (
    EnquirySerializer, CollegeEnquirySerializer, InstructorEnquirySerializer, 
    SummaryEnquirySerializer, InternshipEnquirySerializer
)


logger = logging.getLogger(__name__)

@api_view(['GET', 'POST'])
def enquiry_view(request):
    if request.method == 'POST':
        serializer = EnquirySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Enquiry submitted successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'GET':
        enquiries = Enquiry.objects.all()
        serializer = EnquirySerializer(enquiries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def college_enquiry_view(request):
    if request.method == 'POST':
        serializer = CollegeEnquirySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'College enquiry submitted successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        enquiries = CollegeEnquiry.objects.all()
        serializer = CollegeEnquirySerializer(enquiries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def instructor_enquiry_view(request):
    if request.method == 'POST':
        serializer = InstructorEnquirySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Instructor enquiry submitted successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        enquiries = InstructorEnquiry.objects.all()
        serializer = InstructorEnquirySerializer(enquiries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def summary_enquiry_view(request):
    if request.method == 'POST':
        try:
            serializer = SummaryEnquirySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Summary enquiry submitted successfully!'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error saving summary enquiry: {e}")
            return Response({'error': 'An error occurred while saving the enquiry.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'GET':
        enquiries = SummaryEnquiry.objects.all()
        serializer = SummaryEnquirySerializer(enquiries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def internship_enquiry_view(request):
    if request.method == 'POST':
        serializer = InternshipEnquirySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Internship enquiry submitted successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        enquiries = InternshipEnquiry.objects.all()
        serializer = InternshipEnquirySerializer(enquiries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
