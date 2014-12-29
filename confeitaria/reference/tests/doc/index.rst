=====================================================
Confeitaria reference tests
=====================================================

Welcome to Confeitaria's documentation! Confeitaria is a Web framework for
Python whose main purpose is to test some hypothesis and possibilities about
Web development. Those hypothesis are the `principles`_ behind Confeitaria.

This package provides tests for ensuring any Confeitaria implementation should
have a common set of behaviors.

How to use the Confeitaria reference tests
==========================================

You should install the Confeitaria reference tests with ``pip``::

    $ pip install confeitaria-reference-tests

Yet, since you are supposed to be writing a Confeitaria compliant framework,
it would be better to add ``confeitaria-reference-tests`` as a dependency in
your setup file. For example, if you use ``setuptools``, you can do the
following::

    setup(
        name = "my-confeitaria-impl",
        version = "0.1",
        # ...
        tests_require = ['confeitaria-reference-tests>=0.1']
    )

Extending the reference tests
-----------------------------

Once you have this package available, your new test case should extend the 
``confeitaria.reference.tests.TestReference`` test case. Also, your test case
should implement the ``get_server()`` method. This method should expect a page
object as its argument, and return some object that respect the ``with``
protocol in a way that:

    * in the ``__enter__()`` method, an HTTP server is asynchronously started at
      port 8080, running the Confeitaria implementation being tested; and
    * in the ``__exit__()`` method, the HTTP server is stopped.

For example, let us suppose you have a confeitaria implementation that runs
pm Django. You can write the following class to follow the rules above::

    >>> import multiprocessing
    >>> class DjangoServer(object):
    ...     sef __init__(self, page):
    ...         self.page = page
    ...         self.config = {
    ...             # Port 8080 mandatory
    ...             'port': 8080,
    ...             # Page passed as a config argument
    ...             'page': self.page
    ...         }
    ...     def __enter__(self):
    ...         from django.core.management import setup_environ, call_command
    ...         setup_environ(self.config)
    ...         self.process = multiprocessing.Process(
    ...             target=call_command, args=('runserver',)
    ...         )
    ...         self.process.start()
    ...         time.sleep(1)
    ...     def __exit__(self, type, value, traceback):
    ...         self.process.terminate()
    ...         self.process = None

Then your test would be this way:

    >>> from confeitaria.reference.tests import TestReference
    >>> class TestConfeitariaOnDjango(TestReference):
    ...     def get_server(self, page):
    ...         return DjangoServer(page)

Now all tests will run on your implementation.
 

