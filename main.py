# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
class TestCase(object):
    pass


class WasRun(TestCase):

    def __init__(self, name):
        self.name = name
        self.wasRun = None

    def run(self):
        method = getattr(self, self.name)
        method()

    def testMethod(self):
        self.wasRun = 1


if __name__ == '__main__':
    test = WasRun("testRun")
    print test.wasRun
    test.run()
    print test.wasRun
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
