

from unittest.main import TestProgram

from .runner import UtterlessTextTestRunner


class UtterlessTestProgram(TestProgram):

    def __init__(self, *args, **kwargs):
        kwargs["testRunner"] = UtterlessTextTestRunner
        super().__init__(*args, **kwargs)


if __name__ == "__main__":
    UtterlessTestProgram(module=None)
