"""Test pytest integration."""
import subprocess
import unittest


class PyTestPluginTestCase(unittest.TestCase):
    """Tests around pytest integration."""
    def test_healthcheck_select(self):
        """py.test with '-m healthcheck' selects healthchecks."""
        process = subprocess.Popen(
            [
                'py.test',
                '-m',
                'healthcheck',
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

    def test_healthcheck_deselect(self):
        """py.test with '-m "not healthcheck" does not select healthchecks."""
        process = subprocess.Popen(
            [
                'py.test',
                '-m',
                'not healthcheck',
                'hospital/healthchecks/predictable.py',
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        exit_code = process.wait()
        self.assertEqual(exit_code, 0)
        stdout = str(process.stdout.read())
        self.assertIn('collected 1 items', stdout)
        self.assertIn('===== 1 deselected in ', stdout)
