# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
class TestCase(object):
    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()


class TestCaseTest(TestCase):
    def testRunning(self):
        test = WasRun("testMethod")
        test.run()
        assert (test.wasRun)

    def testSetUp(self):
        test = WasRun("testMethod")
        assert (not test.wasRun)
        test.run()


class WasRun(TestCase):

    def __init__(self, name):
        self.wasRun = None
        TestCase.__init__(self, name)

    def setUp(self):
        self.wasRun = None

    def testMethod(self):
        self.wasRun = 1



if __name__ == '__main__':
    TestCaseTest("testRunning").run()
    # test = WasRun("testRun")
    # print test.wasRun
    # test.run()
    # print test.wasRun
