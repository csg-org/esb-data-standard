ESB File Structure
==================

CSV files must be comma-delimited, UTF-8 (with BOM ommitted) .txt files, named
according to the specification.

Data Types
----------

Each ``field`` belongs to a particular data type. These data types constraint
the allowed values for a particular field. For example, a field of type ``date``
must follow the conventions of a `ISO 8601`_. 

array
^^^^^

An ``array`` is used to store multiple values in a single field.

.. code-block:: 
::
    [""first-value"",""second-value""]

boolean
^^^^^^^

A `boolean`_ represents a true or false value. Possible values are **true** or 
**false**.

date
^^^^

All dates in the ESB feed must conform to the `ISO 8601`_ standard on dates. The
format model of such a date is ``YYYY-MM-DD``. 

string
^^^^^^

A string is a sequence of characters. Most fields in the ESB Data Standard are
strings. Be sure to read the documentation for each string field, as some
fields only allow values that are specified in an enumerated list.
