"""Test pytest integration."""
import subprocess
import unittest


class PyTestPluginTestCase(unittest.TestCase):
    """Tests around pytest integration."""
    def test_healthcheck_marker(self):
        "py.test -m healthcheck hospital/healthchecks/predictable runs 1 test."
        process = subprocess.Popen(
            [
                'py.test',
                '-m "healthcheck"',
                'hospital/healthchecks/predictable.py',
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        exit_code = process.wait()
        self.assertEqual(exit_code, 0)
        stdout = str(process.stdout.read())
        self.assertIn('collected 1 items', stdout)
        self.assertIn('===== 1 passed in ', stdout)
