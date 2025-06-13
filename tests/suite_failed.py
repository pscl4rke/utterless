

import logging
import unittest


class TestCase(unittest.TestCase):

    def test_that_passes(self):
        value = "LOGGED MESSAGE"
        logging.critical("Critical notification of %s", value)
        logging.error("Error notification of %s", value)
        logging.warning("Warning notification of %s", value)
        logging.info("Info notification of %s", value)
        logging.debug("Debug notification of %s", value)
        self.assertTrue(False)
