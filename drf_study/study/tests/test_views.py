import json

import pytest

from drf_study.study.models import Study


@pytest.mark.django_db
def test_add_movie(client):
    study = Study.objects.all()
    assert len(study) == 0

    resp = client.post(
        "/api/study/",
        {
            "title": "Pythonico",
            "category": "Pythonista",
            "description": "Python do sucesso",
        },
        content_type="application/json"
    )
    assert resp.status_code == 201
    assert resp.data["title"] == "Pythonico"
    study = Study.objects.all()
    assert len(study) == 1
