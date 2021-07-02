from pygadgets.ext.ceidg import get_companies


def test_get_companies():
    assert len(get_companies()['firmy']) > 0