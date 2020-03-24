Hire Test
=========

A simple `flask <https://flask.palletsprojects.com/en/1.1.x/>`_ app that serves
a single "Hello World" page.

It depends on the python package `xmlsec
<https://pythonhosted.org/xmlsec/index.html>`_. It again depends on the system
library `XMLsec <https://www.aleksey.com/xmlsec/>`_. It is only chosen because
it requires an additional system package. There is no need to understand how it
works.

The service should be served by `gunicorn <https://gunicorn.org/>`_.

The assignment is to create a ``Dockerfile`` ready for a production
workload. Assume there is a reverse-proxy in front and the server is a single
Ubuntu server running the standard Docker daemon.
