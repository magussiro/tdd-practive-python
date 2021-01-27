from main import TestCase, WasRun, TestResult


class TestCaseTest(TestCase):
    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert ("setUp testMethod tearDown " == test.log)

    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert ("1 run, 0 failed" == result.summary())

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        result = test.run()
        assert ("1 run 1 failed" == result.summary())

    def testFailedResultFomatting(self):
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert ("1 run, 1 failed" == result.summary())


if __name__ == '__main__':
    TestCaseTest("testFailedResult").run()
