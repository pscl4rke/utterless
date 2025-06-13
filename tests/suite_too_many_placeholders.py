

import logging
import unittest


class TestCase(unittest.TestCase):

    def test_behaviour(self):
        # This is to avoid
        #   "TypeError: not enough arguments for format string"
        # if the developer got the wrong number of percent signs
        logging.debug("TEXT-COMES-BEFORE")
        logging.debug("%s %s %s %s", 1, 2)
        logging.debug("TEXT-COMES-AFTER")
        self.assertTrue(False)
