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


@pytest.mark.django_db
def test_add_invalid_json(client):
    study = Study.objects.all()
    assert len(study) == 0

    resp = client.post(
        "/api/study/",
        {},
        content_type="application/json"
    )
    assert resp.status_code == 400

    study = Study.objects.all()
    assert len(study) == 0


@pytest.mark.django_db
def test_add_invalid_json_keys(client):
    study = Study.objects.all()
    assert len(study) == 0

    resp = client.post(
        "/api/study/",
        {
            "title": "Python",
            "category": "loop"
            },
        content_type="application/json"
    )
    assert resp.status_code == 400

    study = Study.objects.all()
    assert len(study) == 0


def test_get_single_study(client):
    study = Study.objects.create(
        title='Docker',
        category='Virtualization',
        description="comandos mais utilizados"
    )
    resp = client.get(f"/api/study/{study.id}/")
    assert resp.status_code == 200
    assert resp.data["title"] == "Docker"
