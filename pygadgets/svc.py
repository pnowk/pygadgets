from . import LOCAL_DIR, join
from .ext.ceidg import iter_pages
import pickle
import logging

log = logging.getLogger(__name__)


def dump_companies(numpages=None):
    log.info('dumping companies')
    pages = iter_pages(numpages, expand=True)
    for ix, page in enumerate(pages):
        with open(join(LOCAL_DIR, 'data', "co_page_" + str(ix) + ".pkl"), "wb") as f:
            log.info(f"dumping page {ix} of length {len(page)}")
            pickle.dump(page, f)
