from main import TestCase, WasRun, TestResult


class TestSuit:
    def __init__(self):
        self.tests = []

    def add(self, test):
        self.tests.append(test)

    def run(self, result):
        for test in self.tests:
            test.run(result)


class TestCaseTest(TestCase):
    def testTemplateMethod(self):
        test = WasRun("testMethod")
        result = TestResult()
        test.run(result)
        assert ("setUp testMethod tearDown " == test.log)

    def testResult(self):
        test = WasRun("testMethod")
        result = TestResult()
        test.run(result)
        assert ("1 run, 0 failed" == result.summary())

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        result = TestResult()
        test.run(result)
        assert ("1 run 1 failed" == result.summary())

    def testFailedResultFomatting(self):
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert ("1 run, 1 failed" == result.summary())

    def testSuite(self):
        suite = TestSuit()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        result = TestResult()
        suite.run(result)
        assert ("2 run, 1 failed" == result.sumary())


if __name__ == '__main__':
    suite = TestSuit()
    suite.add(TestCaseTest("testTemplateMethod"))
    suite.add(TestCaseTest("testTesult"))
    suite.add(TestCaseTest("testFailedResultFormatting"))
    suite.add(TestCaseTest("testFailedResult"))
    suite.add(TestCaseTest("testSuit"))
    # print TestCaseTest("testTemplateMethod").run().summary()
    # print TestCaseTest("testResult").run().summary()
    # print TestCaseTest("testFailedResultFormatting").run().summary()
    # print TestCaseTest("testFailedResult").run().summary()
