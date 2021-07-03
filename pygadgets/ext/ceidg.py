import requests
from requests.adapters import HTTPAdapter
from pygadgets import config
from dataclasses import dataclass
import logging


BASEURL = "https://dane.biznes.gov.pl/api/ceidg/v1"

headers = {"Authorization": "Bearer " + config.PYGADGETS_CEIDG_API_TOKEN}

log = logging.getLogger(__name__)

_session = None
MAX_RETRIES = 3


@dataclass
class Company:
    name: str
    address: dict
    status: str
    url: str
    details: dict


def get_session():
    global _session
    if _session is not None:
        log.debug("using cached session")
        return _session

    session = requests.Session()
    session.headers.update(headers)
    session.mount(prefix=BASEURL, adapter=HTTPAdapter(max_retries=MAX_RETRIES))
    _session = session
    return session


def make_request(query):
    return get_session().get(query).json()


def get_first_page():
    url = BASEURL + "/firmy?limit=50"
    return make_request(url)


def expand_company(co):
    co.details = make_request(co.url)
    return co


def prepare(raw_page, expand=False):
    companies = []
    for co in raw_page:
        c = Company(co["nazwa"], co["adresDzialanosci"], co["status"], co["link"], None)
        if expand:
            c = expand_company(c)
        companies.append(c)
    return companies


def iter_pages(numpages=None, expand=True):
    pagecount = 0
    page = get_first_page()
    while True:
        try:
            log.info(f"getting page {pagecount}")
            prepared = prepare(page["firmy"], expand)
            yield prepared
            next_link = page["links"]["next"]
            log.debug(f"next link {next_link}")
            print(next_link)
            page = make_request(next_link)
        except Exception as e:
            log.info(f"cannot get next page. ending. {str(e)}")
            break
        else:
            pagecount += 1
            if numpages and (pagecount >= numpages):
                log.info("maxpage reached. ending.")
                break
