:tocdepth: 2
API
===

This part of the documentation lists the full API reference of all classes and functions.

WSGI
----

.. autoclass:: reinn.wsgi.ApplicationLoader
   :members:
   :show-inheritance:

Config
------

.. automodule:: reinn.config

.. autoclass:: reinn.config.application.Application
   :members:
   :show-inheritance:

.. autoclass:: reinn.config.redis.Redis
   :members:
   :show-inheritance:

.. automodule:: reinn.config.gunicorn

CLI
---

.. automodule:: reinn.cli

.. autofunction:: reinn.cli.cli.cli

.. autofunction:: reinn.cli.utils.validate_directory

.. autofunction:: reinn.cli.serve.serve

App
---

.. automodule:: reinn.app

.. autofunction:: reinn.app.asgi.on_startup

.. autofunction:: reinn.app.asgi.on_shutdown

.. autofunction:: reinn.app.asgi.get_application

.. automodule:: reinn.app.router

Controllers
~~~~~~~~~~~

.. automodule:: reinn.app.controllers

.. autofunction:: reinn.app.controllers.ready.readiness_check

Models
~~~~~~

.. automodule:: reinn.app.models

Views
~~~~~

.. automodule:: reinn.app.views

.. autoclass:: reinn.app.views.error.ErrorModel
   :members:
   :show-inheritance:

.. autoclass:: reinn.app.views.error.ErrorResponse
   :members:
   :show-inheritance:

Exceptions
~~~~~~~~~~

.. automodule:: reinn.app.exceptions

.. autoclass:: reinn.app.exceptions.http.HTTPException
   :members:
   :show-inheritance:

.. autofunction:: reinn.app.exceptions.http.http_exception_handler

Utils
~~~~~

.. automodule:: reinn.app.utils

.. autoclass:: reinn.app.utils.aiohttp_client.AiohttpClient
   :members:
   :show-inheritance:

.. autoclass:: reinn.app.utils.redis.RedisClient
   :members:
   :show-inheritance:
