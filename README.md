# django-int-to-roman

A simple Django project that converts an integer to a roman numeral. Django 1.8
and Python 2.7.

## Install project and dependencies

- Clone the repository:

```
git clone git@github.com:danielnaab/django-int-to-roman.git
cd django-int-to-roman
```

Create a `virtualenv`, using `virtualenvwrapper` (or alternative).
If python-2.7 is not your default Python, specify it as a parameter:

```
mkvirtualenv --no-site-packages int-to-roman
```

- Install the dependencies:

```
pip install -r requirements-dev.txt
```

*OR:*

```
pip install -r requirements.txt
```

## Unit testing

The `int_to_roman.lib.integer_to_roman` function, which is responsible for the
actual unit conversion, is tested by the `int_to_roman.tests` module. The test
verifies that all numbers in the inclusive range (1, 3999) convert correctly.
This test may be run with:

```
./manage.py test
```

## Running a development server

- Start a local development server:

```
./manage.py runserver
```

- Optionally, specify a `DJANGO_SETTINGS_MODULE` (`local` is the default):

```
export DJANGO_SETTINGS_MODULE=int_to_roman.settings.local
export DJANGO_SETTINGS_MODULE=int_to_roman.settings.production
```

## Project outline

- Because this is a simple Django project, there is no reason for the use of
"apps". The sole URL is specified in the root `urlpatterns`, and the role view
is in a root `views.py`.

- Settings are modularized into a package, with `defaults.py` specifying the
base settings and environment-specific settings in separate modules.

- To demonstrate a potential caching strategy, the form `POST` redirects to a
formal URL pattern with the integer specified as a URL parameter. If this were
a heavily used application and the generation of the response were expensive,
an http caching layer such as Varnish could be placed in front of the web
server to reduce server load. This could further be made more efficient by
skipping the `POST` altogether and setting the URL in the browser via the
`window.history` object, with a fall-back to a `POST` when Javascript is
disabled in the browser.
