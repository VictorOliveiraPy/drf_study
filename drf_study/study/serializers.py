from rest_framework import serializers

from .models import Study


class StudySerializer(serializers.ModelSerializer):

    class Meta:
        model = Study
        fields = [
            'id',
            'title',
            'category',
            'description'
        ]
        read_only_fields = (
            'id',
            'created_date',
            'updated_date'
        )
