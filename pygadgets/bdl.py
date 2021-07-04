from .util import SessionHandler as handler
from . import config

BASEURL = "https://bdl.stat.gov.pl/api/v1"


def _session():
    auth = ("apikey", config.PYGADGETS_BDL_API_KEY)
    return handler.get_session(prefix=BASEURL, auth=auth)


def get_subjects():
    return handler.make_request(_session(), BASEURL + "/subjects?lang=en&format=json")
