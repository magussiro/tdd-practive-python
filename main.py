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
        self.tearDown()

    def tearDown(self):
        pass


class TestCaseTest(TestCase):
    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert ("setUp testMethod tearDown " == test.log)


class WasRun(TestCase):

    def __init__(self, name):
        self.wasRun = None
        TestCase.__init__(self, name)

    def setUp(self):
        self.wasRun = None
        self.log = 'setUp '

    def testMethod(self):
        self.log = self.log + "testMethod "

    def tearDown(self):
        self.log = self.log + "tearDown "


if __name__ == '__main__':
    TestCaseTest("testTemplateMethod").run()
