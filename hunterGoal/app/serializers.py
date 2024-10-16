from rest_framework import serializers
# from ...models import *
from app.models import * 


class EnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquiry
        fields = '__all__'

class CollegeEnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = CollegeEnquiry
        fields = '__all__'

class InstructorEnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = InstructorEnquiry
        fields = '__all__'

class SummaryEnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = SummaryEnquiry
        fields = '__all__'

class InternshipEnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = InternshipEnquiry
        fields = '__all__'

