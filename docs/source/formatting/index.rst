ESB Formatting
==============

.. contents::
   :local:

ESB File Structure
------------------

The CSV file must be comma-delimited, UTF-8 encoded (with BOM omitted), and named
according to the `CSV Documentation`_.

Header Row
----------

The first line of the file, or header row, must conform to the following:

- The CSV file must include a header row containing a comma-delimited list of all data fields, including unused fields.
- All fields names must be in the same letter casing as they appear in the `CSV documentation`_ (e.g. ``BallotReturnDate`` is acceptable, but ``ballotreturndate`` is not).
- All fields must be emitted in the order they appear in the `CSV documentation`_.

Control Characters
------------------

The CSV file must be free of control characters, except for newlines, which should 
follow UNIX syntax (i.e. ``\n``).

Missing Values
--------------

If a data point specified by a field is unavailable, place the value ``na`` in
that field. Note that:

- ``na`` should not be used in a field when a value is not expected, such as an ``OtherType``, when the base field is not set to ``other``.
- ``na`` must not be used in required fields.

Data Types
----------

Each ``field`` belongs to a particular data type. These data types constrain
the allowed values for a particular field. For example, a field of type ``date``
must follow the conventions of a `ISO 8601`_. 

array
^^^^^

An ``array`` is used to store multiple values in a single field.

.. code-block:: text

    [""first-value"",""second-value""]

Even if a field only contains a single value, it still must be surrounded by 
brackets.

boolean
^^^^^^^

A ``boolean`` represents a true or false value. Possible values are ``true`` or 
``false``.

date
^^^^

All dates in the ESB feed must conform to the `ISO 8601`_ standard on dates. The
format model of such a date is ``YYYY-MM-DD``. 

string
^^^^^^

A ``string`` is a sequence of characters. Most fields in the ESB Data Standard are
strings. Be sure to read the documentation for each ``string`` field, as some
fields only allow values that are specified in an enumerated list. String fields
should be free of leading or training whitespace.

.. _CSV documentation: ../csv/
.. _ISO 8601: https://en.wikipedia.org/wiki/ISO_8601
