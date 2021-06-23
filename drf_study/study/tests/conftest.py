import pytest

from drf_study.study.models import Study


@pytest.fixture(scope='function')
def add_study():
    def __add_study(title, category, description):

        study = Study.objects.create(
            title=title,
            category=category,
            description=description,
        )
        return study
    return __add_study
