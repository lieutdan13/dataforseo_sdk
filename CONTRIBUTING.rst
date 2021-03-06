.. highlight:: shell

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/lieutdan13/dataforseo_sdk/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it. Also look at the
TODO section in the README.rst for features.

Write Documentation
~~~~~~~~~~~~~~~~~~~

DataForSEO SDK could always use more documentation, whether as part of the
official DataForSEO SDK docs, in docstrings, or even on the web in blog posts,
articles, and such. See the Getting Started section below for instructions on
how to build the documentation locally.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/lieutdan13/dataforseo_sdk/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `dataforseo_sdk` for local development.

1. Fork the `dataforseo_sdk` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/dataforseo_sdk.git

3. Install your local copy into a virtualenv. This is how you set up your fork for local development::

    $ cd dataforseo_sdk/
    $ python -m venv venv
    $ source venv/Scripts/activate
    $ pip install .
    $ pip install .[test]

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass black and the
   tests, including testing other Python versions with tox::

    $ black --check dataforseo_sdk tests
    $ pytest
    $ safety
    $ tox

   To get black and tox, just pip install them into your virtualenv.

6. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the GitHub website.

Building the Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~

After making contributions to documentation, it's important to build and view the
changes locally, before submitting a pull request.

Here are the instructions on how to build and preview the documentation.

1. Change directory into the root of the project
2. Run `pip install -r requirements_dev.txt` to install the development requirements
3. Run `make docs`
4. A browser should pop-up with the built docs. If not, you can open your browser of
   choice and navigate to `docs/_build/html/index.html`.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The pull request should work for Python 3.7, 3.8, 3.9, and 3.10, and for PyPy. Check
   https://github.com/lieutdan13/dataforseo_sdk/pulls
   and make sure that the tests pass for all supported Python versions.

Tips
----

To run a subset of tests::

$ pytest tests.test_dataforseo_sdk


Deploying
---------

A reminder for the maintainers on how to deploy.
Make sure all your changes are committed (including an entry in HISTORY.rst).
Then run::

$ bump2version patch # possible: major / minor / patch
$ git push
$ git push --tags

Travis will then deploy to PyPI if tests pass.
