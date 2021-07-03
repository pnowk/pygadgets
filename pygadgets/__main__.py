

import sys
import logging
from .svc import dump_companies

log = logging.getLogger(__name__)

if __name__ == "__main__":
    try:
        args = sys.argv[1:]
        if '--dump' in args:
            numpages = None
            if '--num' in args:
                numpages = int(args[2])
            dump_companies(numpages)
    except KeyboardInterrupt:
        log.info('interrupted by the user. exiting.')
        sys.exit(1)

