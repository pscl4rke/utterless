

import unittest

import subprocess
import sys


def run(modulename):
    return subprocess.run(
        [sys.executable, "-m", "utterless", modulename],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


class TestSubprocesses(unittest.TestCase):

    def test_suite_good(self):
        proc = run("suite_good")
        self.assertEqual(proc.returncode, 0)
        output = proc.stdout.decode()
        self.assertIn("\nOK\n", output)
        self.assertNotIn("LOGGED MESSAGE", output)

    def test_suite_failed(self):
        proc = run("suite_failed")
        self.assertNotEqual(proc.returncode, 0)
        output = proc.stdout.decode()
        self.assertIn("\nFAILED (failures=1)\n", output)
        self.assertIn("LOGGED MESSAGE", output)
        self.assertIn("Critical notification", output)
        self.assertIn("Debug notification", output)
