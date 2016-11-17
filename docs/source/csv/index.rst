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

Data Fields
-----------
The following fields are possible data points for each transaction that the standard hopes to collect.

.. include:: standard.rst.part

.. _Uniformed and Overseas Citizen Absentee Voting Act: https://www.fvap.gov/info/laws/uocava
.. _Voting Information Project's: https://votinginfoproject.org
