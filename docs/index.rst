.. pyformmail documentation master file, created by
   sphinx-quickstart on Mon Jan  1 04:23:27 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pyformmail's documentation!
======================================

pyformmail is a near-drop-in replacement for `FormMail.pl`_. This package provides a Python module ``PyFormMail`` designed to be executed from a WSGI environment.

As with the original, this is a generic HTML form to email gateway that parses the results of any form and sends them to the specified users. There are many options that can be specified in either a configuration file or within each form, allowing flexible use even on one ``PyFormMail`` instance.

.. _FormMail.pl: http://www.scriptarchive.com/formmail.html

.. _user-docs:

.. toctree::
   :maxdepth: 1
   :caption: User documentation
   
   getting_started
   configuration

Source and support
------------------

- Source code: https://git.vishwin.info/pyformmail.git/
- github mirror: https://github.com/vishwin/pyformmail

Report bugs, patches, questions, etc to `email`_. Paid commercial support is available through `Wahgwan Industry Limited`_.

.. _email: https://vishwin.info/Contact
.. _Wahgwan Industry Limited: https://wahgwan.xyz/

Licence
-------

This project is licensed under the three-clause BSD licence.
