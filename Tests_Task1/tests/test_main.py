import pytest
from Tests_Task1.main import add_new_doc, get_doc_shelf, get_doc_owner_name, delete_doc

fixtures = [
    ('15 321', 'pass', 'Evgen', '4'),
    ('16 112', 'inv', 'Ramil', '2'),
    ('17 401', 'card', 'Nikol', '3')
]


@pytest.mark.parametrize('doc_number, doc_type, doc_owner_name, doc_shelf_number', fixtures)
def test_add_new_doc(doc_number, doc_type, doc_owner_name, doc_shelf_number):
    assert add_new_doc(doc_number, doc_type, doc_owner_name, doc_shelf_number) == True


@pytest.mark.parametrize('doc_number, doc_type, doc_owner_name, doc_shelf_number', fixtures)
def test_get_doc_shelf(doc_number, doc_type, doc_owner_name, doc_shelf_number):
    assert get_doc_shelf(doc_number) == doc_shelf_number


@pytest.mark.parametrize('doc_number, doc_type, doc_owner_name, doc_shelf_number', fixtures)
def test_get_doc_owner_name(doc_number, doc_type, doc_owner_name, doc_shelf_number):
    assert get_doc_owner_name(doc_number) == doc_owner_name


@pytest.mark.parametrize('doc_number, doc_type, doc_owner_name, doc_shelf_number', fixtures)
def test_delete_doc(doc_number, doc_type, doc_owner_name, doc_shelf_number):
    delete_doc(doc_number)
    assert get_doc_owner_name(doc_number) is None
