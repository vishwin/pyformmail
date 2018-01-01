Configuration
=============

This document details all configuration variables.

Mail server settings
--------------------

.. py:data:: MAIL_SERVER

   The domain name or IP address of the SMTP server used to deliver mail. Defaults to ``localhost``.

.. py:data:: MAIL_PORT

   The port that the SMTP server listens on. Defaults to ``0``, which equates to the default SMTP port ``25``.

.. py:data:: MAIL_USE_TLS

   Boolean to determine whether SMTP sessions shall include TLS encryption with STARTTLS. Defaults to ``False``.

.. py:data:: MAIL_USERNAME

   If the SMTP server requires authentication, the username to authenticate as. Defined as an empty string by default.

.. py:data:: MAIL_PASSWORD

   If the SMTP server requires authentication, the password to authenticate as. Defined as an empty string by default.

Form settings
-------------

The following is a mapping between HTML form field names and their equivalent configuration file variables prefixed with ``FM_``:

.. literalinclude:: ../PyFormMail/fieldmap.py

Necessary form fields
~~~~~~~~~~~~~~~~~~~~~

.. py:data:: FM_RECIPIENT

Optional form fields
~~~~~~~~~~~~~~~~~~~~

.. py:data:: FM_SUBJECT

.. py:data:: FM_EMAIL

.. py:data:: FM_REALNAME

.. py:data:: FM_REDIRECT

.. py:data:: FM_REQUIRED

.. py:data:: FM_ENV_REPORT

.. py:data:: FM_SORT

.. py:data:: FM_PRINT_CONFIG

.. py:data:: FM_PRINT_BLANK_FIELDS

.. py:data:: FM_TITLE

.. py:data:: FM_RETURN_LINK_URL

.. py:data:: FM_RETURN_LINK_TITLE

.. py:data:: FM_MISSING_FIELDS_REDIRECT

.. py:data:: FM_BACKGROUND

.. py:data:: FM_BGCOLOR

.. py:data:: FM_TEXT_COLOR

.. py:data:: FM_LINK_COLOR

.. py:data:: FM_VLINK_COLOR

.. py:data:: FM_ALINK_COLOR

.. py:data:: FM_COMMENT
