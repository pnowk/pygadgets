from os import stat
from os import listdir, remove
from . import LOCAL_DIR, join, Path
from .ceidg import iter_pages
from .util import lazyproperty
import pickle
import logging

log = logging.getLogger(__name__)
PAGE_SUFF = "_page_"


def _dump_pages(numpages=None, expand=False):
    log.info("dumping companies")
    pages = iter_pages(numpages, expand=expand)
    expanded_suff = "_expanded" if expand else ""
    for ix, page in enumerate(pages):
        with open(
            join(
                LOCAL_DIR, "data", "co" + PAGE_SUFF + str(ix) + expanded_suff + ".pkl"
            ),
            "wb",
        ) as f:
            log.info(f"dumping page {ix} of length {len(page)}")
            pickle.dump(page, f)


class CeidgService:
    @property
    def datafiles(self):
        return [
            join(LOCAL_DIR, "data", f)
            for f in listdir(str(LOCAL_DIR) + "/data")
            if PAGE_SUFF in f
        ]

    @lazyproperty
    def pages(self):
        _pages = []
        for pkl in self.datafiles:
            with open(pkl, "rb") as f:
                records = pickle.load(f)
                _pages.append(records)
        return _pages

    def prepare_dump(self, numpages=None, expand=False, clear=False):
        for f in self.datafiles:
            if clear:
                log.info(f"removing {f}")
                remove(f)
        _dump_pages(numpages, expand)

    def list_companies(self):
        return [co for page in self.pages for co in page]

    def filter_by_name(self, name):
        return [
            co
            for co in self.list_companies()
            if co.name.lower().strip() == name.lower()
        ]
