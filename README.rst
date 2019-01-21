Guess gender from indian names
==============================

Motivation
----------

I was not able to find a open source library that guess gender from
indian names. So made one.

Prerequisites
-------------

-  Python 3.7
-  Pipenv

Development - Setup instructions
--------------------------------

-  Clone this repository.
-  cd to the repo
-  Activate pipenv ``pipenv shell``
-  Install dependencies ``pipenv install``
-  Fire up a python shell and type the following.

.. code:: python

   >>> from guess_indian_gender import IndianGenderPredictor
   >>> i = IndianGenderPredictor()
   >>> i.predict(name="adhi") # returns male

Installation
------------

-  ``pip install guess-indian-gender``

Accuracy
--------

-  Currently the accuracy is 0.88. Any contributions are welcome to
   improve the accuracy.

Changelog
---------

-  When the last letter is considered as a feature for gender detection
   the accuracy is 78%.
-  When the last four letters was considered the accuracy became 88%.

Todo
----

-  [x] Convert to Pip package.
-  [x] Convert to nice oops.
-  [ ] Improve accuracy to 95%.

Dataset credits
---------------

-  https://github.com/mbejda
-  Male names - https://gist.github.com/mbejda/7f86ca901fe41bc14a63
-  Female names - https://gist.github.com/mbejda/9b93c7545c9dd93060bd

License
-------

MIT. See license file for more info