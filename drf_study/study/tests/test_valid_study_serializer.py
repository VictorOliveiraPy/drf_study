from drf_study.study.serializers import StudySerializer


def test_valid_study_serializer():
    valid_serializer_data = {
        "title": "Python",
        "category": "linguagem",
        "description": "Pythonicodms"
    }
    serializer = StudySerializer(
        data=valid_serializer_data
    )
    assert serializer.is_valid()
    assert serializer.validated_data == valid_serializer_data
    assert serializer.data == valid_serializer_data
    assert serializer.errors == {}


def test_invalid_study_serializer():
    invalid_serializer_data = {
        "title": "Python",
        "category": "linguagem",
    }
    serializer = StudySerializer(
        data=invalid_serializer_data
    )
    serializer = StudySerializer(
        data=invalid_serializer_data
    )
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    assert serializer.errors == {"description": ["This field is required."]}
