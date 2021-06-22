import pytest

from drf_study.study.models import Study


@pytest.mark.django_db
def test_study_model():
    study = Study(
       title='Docker',
       description='muito bom',
       category='Virtualization'
    )
    study.save()
    assert study.title == 'Docker'
    assert study.description == 'muito bom'
    assert study.category == 'Virtualization'
    assert study.created_date
    assert study.updated_date
    assert str(study) == study.title
