from pygadgets.ext.ceidg import get_first_page, iter_pages
import pytest


# @pytest.mark.skip('skip for now')
def test_get_first_page():
    assert len(get_first_page()['firmy']) == 50

def test_iter_pages():
    pages = iter_pages(3)
    assert len(list(pages)) == 3



