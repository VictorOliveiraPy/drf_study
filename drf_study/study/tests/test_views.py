import json

from django.urls import reverse

import pytest

from drf_study.study.models import Study


@pytest.mark.django_db
def test_add_movie(client):
    study = Study.objects.all()
    assert len(study) == 0

    resp = client.post(reverse(
        "api/study"),
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

    resp = client.post(reverse(
        "api/study"),
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

    resp = client.post(reverse(
        "api/study"),
        {
            "title": "Python",
            "category": "loop"
            },
        content_type="application/json"
    )
    assert resp.status_code == 400

    study = Study.objects.all()
    assert len(study) == 0

@pytest.mark.django_db
def test_get_single_study(client, add_study):
    study = add_study(
        title='Docker',
        category='Virtualization',
        description="comandos mais utilizados"
    )
    resp = client.get(f"/api/study/{study.id}/")
    assert resp.status_code == 200
    assert resp.data["title"] == "Docker"


def test_get_single_study_incorrect_id(client):
    resp = client.get("/api/study/buuh/")
    assert resp.status_code == 404

@pytest.mark.django_db
def test_get_all_study(client, add_study):

    study_one = add_study(
        title='Django',
        category='Framework',
        description='Web'
    )
    study_two = add_study(
        "Django Framework",
        'Framework',
        'Django best framework'
    )
    resp = client.get(
        reverse('api/study')
    )
    assert resp.data[0]["title"] == study_one.title
    assert resp.data[1]["title"] == study_two.title
