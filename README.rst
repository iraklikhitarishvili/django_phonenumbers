Installation
============

::

    run  pip install django_phonenumbers

Configure settings.py
======================

::

     Add django_phonenumbers to INSTALLED_APPS

manage.py
=========

::

     run manage.py collectstatic

settings.py
===========


.. code:: python

        PHONE_NUMBER_REGION = 'GE'  
        PHONE_NUMBERS_FORMATS_BY_REGION = {
            'GE': {
                'pattern': '(\\d{3})(\\d{2})(\\d{2})(\\d{2})', 'format': '\\1 \\2-\\3-\\4', 'prefix_format': '+%s (%s)'
            },
            'US': {
                'pattern': '(\\d{3})(\\d{3})(\\d{4})', 'format': '\\1 \\2-\\3', 'prefix_format': '+%s (%s)'
            },
        }

- "PHONE_NUMBER_REGION" determines which country region will be selected in admin's corresponding phone number field
- "PHONE_NUMBERS_FORMATS_BY_REGION" is used in "phone_number_format" filter

Model
=====

.. code:: python

    #models.py
    class MyModel(models.Model):
        ...
        phone_number = PhoneNumberField()
        ...

        def __str__(self):
            return str(self.phone_number)

**"phone_number"** field's type will be **"PhoneNumber"**

.. code:: python

    class PhoneNumber:
        def __init__(self, country_code=None, region_code=None, phone_number=None):
            """
            :type country_code: str
            :type region_code: str
            :type phone_number: str
            """
            self.country_code = country_code
            self.google_phone_number = None
            self.region_code = region_code
            self.phone_number = phone_number

"__str__" and "__repr__" functions are overridden to return "country_code"+" "+"phone_number"

**model.fields.PhoneNumberField** is using **form.fields.PhoneNumberField** in admin by default

**model.fields.PhoneNumberField** and **form.fields.PhoneNumberField** is validating and formatting(in national format) entered number



Template example
================

.. code:: html

    <li>
                {{ number.phone_number }}
                // {{ number.phone_number.region_code }}
                // {{ number.phone_number.country_code }}
                // {{ number.phone_number.phone_number }}
                <div>
                    {% load phone_numbers_extra %}
                    <h4>Filter
                        <small>{{ number.phone_number|phone_number_format }}</small>
                    </h4>
                    <h4>Simple tag
                        <small>
                            {% phone_number number.phone_number pattern='(\\d{3})(\\d{3})(\\d{3})' number_format='\\1 \\2-\\3' prefix_format='+%s (%s)' %}
                        </small>
                    </h4>
                </div>
    </li>

**phone_number_format** uses **PHONE_NUMBERS_FORMATS_BY_REGION** from settings.py to determine phone number format

Example
=======
::

'GE': {  'pattern': '(\\d{3})(\\d{2})(\\d{2})(\\d{2})', 'format': '\\1 \\2-\\3-\\4', 'prefix_format': '+%s (%s)'},

- 'GE' : region code
- 'pattern' : ``'(\\d{3})(\\d{2})(\\d{2})(\\d{2})'`` is regex. this regex will split phone number in 4 groups:
    - 3 digits
    - 2 digits
    - 2 digits
    - 2 digits

- 'format' : ``'\\1 \\2-\\3-\\4'`` numbers are groups mentioned above. for example if you want to put last 2 digits in scopes you should write '\\1 \\2-\\3-(\\4)' and result will be xxx xx-xx-(xx)
- 'prefix_format' : '+%s (%s)' first "%s" is country code second mobile operator or city code for example +995 (595) where 995 is my country code and 595 my mobile operator's code you can change formatting fore example '[%s] [%s]' will give [995] [595] this result

with this simple tag you can specify format inline

.. code:: python

    {% phone_number number.phone_number pattern='(\\d{3})(\\d{3})(\\d{3})' number_format='\\1 \\2-\\3' prefix_format='+%s (%s)' %}
