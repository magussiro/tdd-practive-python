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
    def setUp(self):
        self.result = TestResult()

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert ("setUp testMethod tearDown " == test.log)

    def testResult(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert ("1 run, 0 failed" == self.result.summary())

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        test.run(self.result)
        assert ("1 run 1 failed" == self.result.summary())

    def testFailedResultFomatting(self):
        self.result.testStarted()
        self.result.testFailed()
        assert ("1 run, 1 failed" == self.result.summary())

    def testSuite(self):
        suite = TestSuit()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        suite.run(self.result)
        assert ("2 run, 1 failed" == self.result.summary())


if __name__ == '__main__':
    suite = TestSuit()
    suite.add(TestCaseTest("testTemplateMethod"))
    suite.add(TestCaseTest("testTesult"))
    suite.add(TestCaseTest("testFailedResultFormatting"))
    suite.add(TestCaseTest("testFailedResult"))
    suite.add(TestCaseTest("testSuit"))
    result = TestResult()
    suite.run(result)
    print result.summary()
    # print TestCaseTest("testTemplateMethod").run().summary()
    # print TestCaseTest("testResult").run().summary()
    # print TestCaseTest("testFailedResultFormatting").run().summary()
    # print TestCaseTest("testFailedResult").run().summary()
