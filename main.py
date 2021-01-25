# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
class WasRun(object):

    def __init__(self):
        self.wasRun = None

    def testMethod(self):
        self.wasRun = 1


if __name__ == '__main__':
    test = WasRun("testRun")
    print test.wasRun
    test.testMethod()
    print test.wasRun
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
