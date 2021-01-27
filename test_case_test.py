from main import TestCase, WasRun, TestResult


class TestSuit(object):
    def add(self, param):
        pass

    def run(self):
        pass


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

    def testSuite(self):
        suite = TestSuit()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        result = suite.run()
        assert ("2 run, 1 failed" == result.sumary())


if __name__ == '__main__':
    TestCaseTest("testFailedResult").run()
    print TestCaseTest("testTemplateMethod").run().summary()
    print TestCaseTest("testResult").run().summary()
    print TestCaseTest("testFailedResultFormatting").run().summary()
    print TestCaseTest("testFailedResult").run().summary()
