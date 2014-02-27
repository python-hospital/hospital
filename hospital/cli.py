# -*- coding: utf-8 -*-
"""Command-line interface utilities to collect and run healthchecks."""
import argparse
import itertools
import sys
import unittest

from hospital.loading import HealthCheckLoader


def cli_parser(program):
    """Argument parser factory."""
    parser = argparse.ArgumentParser(prog=program)
    parser.add_argument(
        '--discover',
        action='append',
        nargs='*')
    parser.add_argument(
        '--names',
        action='append',
        nargs='*')
    return parser


class HealthCheckProgram(object):
    def __init__(self, discover=[], names=[], modules=[], test_cases=[],
                 runner=None, loader=None, result_class=None, verbosity=1,
                 failfast=False, stream=sys.stderr):
        self.discover = discover
        self.names = names
        self.modules = modules
        self.test_cases = test_cases
        self.verbosity = verbosity
        self.failfast = failfast
        if result_class is None:
            self.result_class = self.default_result_class()
        else:
            self.result_class = result_class
        if loader is None:
            self.loader = self.default_loader()
        else:
            self.loader = loader
        if runner is None:
            self.runner = self.default_runner(
                verbosity=self.verbosity,
                failfast=self.failfast,
                result_class=self.result_class,
                stream=stream)
        else:
            self.runner = runner

    def default_loader(self):
        return HealthCheckLoader()

    def default_runner(self, verbosity=1, failfast=False,
                       result_class=unittest.TextTestResult,
                       stream=sys.stderr):
        return unittest.TextTestRunner(
            verbosity=verbosity,
            failfast=failfast,
            resultclass=result_class,
            stream=stream)

    def default_result_class(self):
        return unittest.TextTestResult

    def load_tests(self):
        """Return a test suite."""
        suite = self.loader.suiteClass()
        for start_dir in self.discover:
            suite.addTest(self.loader.discover(
                start_dir, pattern='*'))
        if self.names:
            suite.addTest(self.loader.loadTestsFromNames(self.names))
        return suite

    def run_tests(self, test_suite):
        """Return result for test suite."""
        result = self.runner.run(test_suite)
        return result

    def __call__(self):
        suite = self.load_tests()
        return self.run_tests(suite)


def main(program=None, args=None, stream=sys.stderr):
    """Collect and run healthchecks, output to stdout and stderr."""
    parser = cli_parser(program)
    arguments = parser.parse_args(args)
    if arguments.discover:
        discover = itertools.chain(arguments.discover)
    else:
        discover = []
    names = itertools.chain(*arguments.names) if arguments.names else []
    app = HealthCheckProgram(discover=discover, names=names, stream=stream)
    app()


if __name__ == '__main__':
    main()
