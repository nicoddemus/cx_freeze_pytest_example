cx_freeze_pytest_example
========================
 
Example on how to embed the [py.test](http://pytest.org) runner into an executable 
using [cx_freeze](http://cx-freeze.readthedocs.org).

This unfortunately is not as straightforward as one hopes, because `pytest` makes heavy use
of dynamic module loading which `cx_freeze` can't resolve by itself.

Solution
--------

Manually include `pytest` and `py` modules (which pytest depends on) by using 
the `build_exe` option in your `setup.py` script:

```python
includes = [    
    '_pytest.doctest',
    '_pytest.pdb',
    '_pytest.unittest',
    '_pytest.capture',
    '_pytest.config',
    # ... lots more
]

setup(
    name="runtests",    
    options={"build_exe": {'includes': includes}},
    # ... other options
)
```

See [setup.py](setup.py) for the complete file.

Example
-------

This repository contains an example that may be used as a sandbox for testing
or playing around.
 
To build it execute (better done in a dedicated virtual environment):

```bash
$ pip install cx_freeze
$ python setup.py build --build-exe bin
```

Running it should produce the usual pytest output:

```bash
$ bin/runtests --pytest --verbose tests
============================= test session starts =============================
platform win32 -- Python 2.7.6 -- py-1.4.22 -- pytest-2.6.0 -- X:\pytest_cx_freeze\bin\runtests.exe
collected 3 items

tests/test_doctest.txt::[doctest] tests/test_doctest.txt PASSED
tests/test_trivial.py@2::test_upper PASSED
tests/test_trivial.py@5::test_lower PASSED
```

Wait, why would you do that?
----------------------------

If you freeze your application using a tool like `cx_freeze` in order to 
distribute it to your end-users, 
it is a good idea to also package your test runner and run your tests using 
the frozen application. 

This way you can detect packaging errors such as dependencies not being 
included into the executable while also allowing you to send test files to
users so they can run them in their machines, which can be invaluable to 
obtain more information about a hard to reproduce bug.