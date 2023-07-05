

import logging
LOG = logging.getLogger("demo")

import unittest

import utterless


def square(value):
    LOG.critical("Critical notification of %s" % value)  # percent
    LOG.error("Error notification of %s" % value)
    LOG.warning("Warning notification of %s" % value)
    LOG.info("Info notification of %s", value)  # not percent
    LOG.debug("Debug notification of %s", value)
    return value * value


class TestDemo(unittest.TestCase):

    def test_correct(self):
        """Docstring will still be shown in output"""
        self.assertEqual(square(3), 9)

    def test_incorrect(self):
        """Docstring will still be shown in output"""
        self.assertEqual(square(3), 10)


if __name__ == "__main__":
    utterless.main()
