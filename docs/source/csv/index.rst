CSV Documentation
=================
.. contents::
   :local:

.. _getting-started:

Getting Started
---------------
If you're a state or local election official reading this, first, thank you for your work and
your interest in the project. The data required to participate in this project is typically
found in absentee voter roster files, voter registration databases, or voter history files.
Sometimes all three...and maybe others. The standard looks to capture `Uniformed and Overseas
Citizen Absentee Voting Act`_ (UOCAVA) transactions, such as:

- when a voter requests a ballot;
- when the application is processed;
- to what country the ballot is sent and when;
- why an application/ballot is rejected; and,
- whether a voter is military or overseas citizen.

To make the process of collecting data easier, this project borrows lessons from the `Voting
Information Project's`_ (VIP's) approach to data collection: use a flat file format for data collection
and push any transformations downstream.

Naming Convention
-----------------
Due to the many issues around elections data collection and cleanliness, much of the data still requires
some form of human oversight. Therefore, having a relatively accessible file naming convention is
beneficial. While this is not a hard-and-fast rule, anyone producing data in this standard should use
the following naming convention, which partially borrows from the `Voting Information Project's`_ documentation.

.. code-block:: none

   esbdata-${ELECTION_DATE}-${STATE}[-${LOCAL}].{csv|zip}

An explanation of each of the segments of the file naming convention above are as follows:

- ``${ELECTION_DATE}`` - The date of the election in `ISO 8601`_ format.
- ``${STATE}`` - The full state name (e.g. Alaska, Arkansas, etc...) and not the abbreviation. If
  there are spaces in the state name, they should be substituted with underscores (e.g. New York ->
  New_York).
- ``${LOCAL}`` (optional) - This additional identifier should be used if the file contains data
  from a specific jurisdiction. As with ``${STATE}`` above, all spaces should be substituted with
  underscores. For example, if the data contained in the file only covers Maricopa County, AZ for
  the November 6, 2012 election, the file name would be
  ``esbdata-2012-11-06-Arizona-Maricopa_County.csv``.
- ``{csv|zip}`` - If the file is an uncompressed CSV document, the extension should be ``.csv``. If
  the file is zipped, the file extension should end with ``.zip``.

For a final example, ``esbdata-2012-11-06-Iowa.zip`` denotes Iowa's data for the Nov 6, 2012 election
that has been compressed.

Data Fields
-----------
The following fields are possible data points for each transaction that the standard hopes to collect.

.. include:: standard.rst.part

.. _Uniformed and Overseas Citizen Absentee Voting Act: https://www.fvap.gov/info/laws/uocava
.. _Voting Information Project's: https://votinginfoproject.org
.. _ISO 8601: https://en.wikipedia.org/wiki/ISO_8601
