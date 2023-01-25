# pytest

## Learning Goals

- Explain how pytest is used to ensure our code works as expected.
- Configure an application to run pytest.
- Describe the structure of a pytest test.
- Execute pytest with flags to ensure its output is what we need.
- Interpret pytest output to find the sources of errors.

***

## Key Vocab

- **Unit Testing**:
- **Test-Driven Development**:
- **Assertion**:

***

## Introduction

pytest is a testing framework in Python that makes it easy to write short,
easy-to-parse tests for applications ranging from a single function to huge
libraries.

***

## pytest Helps You Write Better Programs

pytest is primarily used for a task called **unit testing**. Unit testing is a
provess in which the smalled parts of an application- no matter how large- are
looked at individually and tested to make sure they operate as intended. Testing
is usually carried out by developers themselves, but sometimes by teams of
quality assurance (QA) engineers as well.

Unit tests will typically run on many functions at once with many different
types of input. The number of failures with their descriptions will be returned
to the tester so that they can update any non-functional code. Tests can be run
quickly and as many times as desired. They can also be run on code that doesn't
exist yet- this allows for a process called **test-driven development** (TDD),
where failures are used to inform what code to write next.

### An Example of TDD

Let's say you want to write a function that interpolates into a string: given a
name, it should return "Welcome, name!"

This is fairly simple to write, but even easier to test. Let's start by writing
an assertion that will raise an Exception if the return value of our function
is incorrect. Open up the Python shell and enter the following:

```console
>>> def interpolate_welcome(name):
...     pass
...
>>> assert interpolate_welcome('Guido') == 'Welcome, Guido!'
```

You should see the following output:

```console
# => Traceback (most recent call last):
# =>   File "<stdin>", line 1, in <module>
# => AssertionError
```

This tells us that in the most recent block of code (the assertion), there was
an error on the first line. As this is an assertion, the error is easy enough
to parse out: `interpolate_welcome()` doesn't interpolate the name we pass in!

Let's use that assertion to drive the development of some working code:

```console
>>> def interpolate_welcome(name):
...     return f'Welcome, {name}!'
...
>>> assert interpolate_welcome('Guido') == 'Welcome, Guido!'
```

You should see no output from this assertion- that means that it worked!

Simple assertions are _enough_ for us to do TDD, but they don't give us many
details. We'll see how pytest improves upon this process in just a bit.

***

## What Does a pytest Test Look Like?

While you've worked with several pytest tests up to this point, you may not
have dug into the test files themselves. Let's do that now.

The first thing that we need to do to create an application environment that
supports pytest is include either `pytest.ini` or `setup.py`. pytest generates
its own paths when it is run, and can often struggle to find the files that you
wish to test. The inclusion of these files allows us to specify where pytest
should start building paths. We give it two options: `.`, the root directory,
and `lib`, the application directory.

Once this is set up, we should create a directory to house our tests. This can
be named any valid Python package name (no dashes!), but we recommend making it
clear that it contains test. Ours is contained in `lib/` and is simply called
`testing/`.

We've put a couple of tests inside of `testing`: `test_string.py` and
`function_test.py`. pytest files must be named either starting with "test_" or
ending with "_test". pytest will look in the current directory and every
subdirectory for any files that match this naming pattern and execute any tests
within.

Next up are the tests themselves. (Finally!)

***

## Resources
