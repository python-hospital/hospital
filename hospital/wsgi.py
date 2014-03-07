# -*- coding: utf-8 -*-
"""WSGI utilities to collect and run healthchecks as web service.

.. warning::

   Implementation is not mature, i.e. this part of hospital API may change
   in future releases. That said, it does the job ;)

"""
import json
import unittest
from wsgiref.simple_server import make_server

from hospital.cli import base_parser, HealthCheckProgram, HEALTHCHECKS


class STATUS(object):
    """Pseudo-constant."""
    PASS = 'pass'
    SKIP = 'skip'
    FAIL = 'fail'
    ERROR = 'error'
    EXPECTED_FAILURE = 'expected_failure'
    UNEXPECTED_SUCCESS = 'unexpected_success'


class HealthCheckResult(unittest.TestResult):
    """Collect information about healthchecks."""
    def __init__(self):
        super(HealthCheckResult, self).__init__()
        #: List of successes.
        self.successes = []
        #: A list of results, in order of execution.
        self.results = []

    def addSuccess(self, test):
        super(HealthCheckResult, self).addSuccess(test)
        self.successes.append(test)
        self.results.append((STATUS.PASS, test, None))

    def addError(self, test, err):
        super(HealthCheckResult, self).addError(test, err)
        self.results.append((STATUS.ERROR, test, err))

    def addSkip(self, test):
        super(HealthCheckResult, self).addSkip(test)
        self.results.append((STATUS.SKIP, test, None))

    def addFailure(self, test, err):
        super(HealthCheckResult, self).addFailure(test, err)
        self.results.append((STATUS.FAIL, test, err))

    def addExpectedFailure(self, test, err):
        super(HealthCheckResult, self).addExpectedFailure(test, err)
        self.results.append((STATUS.EXPECTED_FAILURE, test, err))

    def addUnexpectedSuccess(self, test):
        super(HealthCheckResult, self).addUnexpectedSuccess(test)
        self.results.append((STATUS.UNEXPECTED_SUCCESS, test))


class HealthCheckRunner(object):
    def __init__(self, result_class=HealthCheckResult):
        self.result_class = result_class

    def run(self, suite):
        result = self.result_class()
        suite.run(result)
        return result


class HealthCheckApp(HealthCheckProgram):
    """A basic WSGI application to expose results of healthchecks."""
    def default_result_class(self):
        return HealthCheckResult

    def default_runner(self, verbosity=1, failfast=False,
                       result_class=unittest.TextTestResult,
                       stream=None):
        return HealthCheckRunner(
            result_class=self.result_class)

    def passed(self, result):
        """Return ``True`` if result 'passed', i.e. has no fail or error."""
        return not (
            result.errors or
            result.failures or
            result.unexpectedSuccesses)

    def title(self, result):
        """Return 'pass' or 'fail' as string."""
        return 'pass' if self.passed(result) else 'fail'

    def summary(self, result):
        """Return summary dict."""
        return {
            'total': result.testsRun,
            STATUS.PASS: len(result.successes),
            STATUS.EXPECTED_FAILURE: len(result.expectedFailures),
            STATUS.SKIP: len(result.skipped),
            STATUS.ERROR: len(result.errors),
            STATUS.FAIL: len(result.failures),
            STATUS.UNEXPECTED_SUCCESS: len(result.unexpectedSuccesses),
        }

    def get_test_title(self, test):
        """Return title for test object."""
        return test.shortDescription() or str(test)

    def details(self, result):
        """Generate report details dict."""
        for status, test, context in result.results:
            report = {
                'test': self.get_test_title(test),
                'status': status,
            }
            if context is not None:
                report['context'] = u'{context}'.format(context=context)
            yield report

    def __call__(self, environ, start_response):
        suite = self.load_tests()
        result = self.run_tests(suite)
        success = not (
            result.errors or result.failures or result.unexpectedSuccesses)
        body = {
            'status': self.title(result),
            'summary': self.summary(result),
            'details': [line for line in self.details(result)],
        }
        body = json.dumps(body, indent=4, separators=(',', ': '))
        status = '200 OK' if success else '500 Error'
        headers = [
            ('Content-Type', 'application/json; charset=utf-8'),
            ('Content-Length', str(len(body))),
        ]
        start_response(status, headers)
        return [body]


def wsgi_parser(program=None):
    parser = base_parser(program)
    parser.add_argument(
        '--port',
        action='store',
        nargs='?',
        type=int,
        default='1515',
        help="Port for webserver.",
    )
    return parser


#: WSGI application endpoint.
application = HealthCheckApp(discover=HEALTHCHECKS)


def main(program=None, args=None):
    parser = wsgi_parser(program)
    arguments = parser.parse_args(args)
    if arguments.healthchecks:
        healthchecks = arguments.healthchecks
    else:
        healthchecks = HEALTHCHECKS
    app = HealthCheckApp(discover=healthchecks)
    httpd = make_server('', arguments.port, app)
    server_address = httpd.socket.getsockname()
    print("Serving on {ip} port {port}...".format(
        ip=server_address[0],
        port=server_address[1]))
    httpd.serve_forever()


if __name__ == '__main__':
    main()
