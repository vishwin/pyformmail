Getting started
===============

This document will show you how to get up and running with pyformmail.

Install
-------

The pyformmail source code lives in a git repository. You can get a local copy by running::

    $ git clone https://git.vishwin.info/pyformmail.git

If you prefer using the github mirror, run one of these two::

    $ git clone https://github.com/vishwin/pyformmail.git
    $ git clone git@github.com:vishwin/pyformmail.git

Currently, this project is not yet available on `PyPi/Cheeseshop`_, but you can still install the package via ``pip`` by incorporating the ``git clone``::

    $ pip install git+https://git.vishwin.info/pyformmail.git

.. _PyPi/Cheeseshop: https://pypi.python.org

Basic configuration
-------------------

The package comes with a default set of configuration variables in ``default.cfg``:

.. literalinclude:: ../PyFormMail/default.cfg

Variables prefixed with ``MAIL_`` concern the SMTP server used for the actual mail delivery. Those with ``FM_`` can be set either in a config file or directly in the HTML form. Note that values set in the HTML form will override those set in the ``FM_`` variables.

More information regarding each variable is documented in the next section.
