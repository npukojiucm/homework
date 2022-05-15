import pytest
from Tests_Task1.main import show_all_docs_info

old_fixtures = [
    ('passport "2207 876234" "Василий Гупкин"'),
    ('invoice "11-2" "Геннадий Покемонов"'),
    ('insurance "10006" "Аристарх Павлов"')
]


@pytest.mark.parametrize('fixtures', old_fixtures)
def test_show_document_info(fixtures):
    assert fixtures in show_all_docs_info()
