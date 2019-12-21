#!./venv/bin/python
# ------------------------------------------------------------------------------
#  Copyright (c) 2019. Anas Abu Farraj.
# ------------------------------------------------------------------------------
"""Python playground."""


class SomeClass:
    @classmethod
    def class_name(cls):
        return cls.__name__


myClass = SomeClass()

print(myClass.class_name())  # SomeClass
