"""This project was generated with fastapi-mvc."""
import logging

from reinn.wsgi import ApplicationLoader
from reinn.version import __version__

# initialize logging
log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())

__all__ = ("ApplicationLoader", "__version__")
