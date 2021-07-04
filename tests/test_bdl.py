from pygadgets.bdl import get_subjects


def test_subject():
    assert get_subjects().status_code == 200
