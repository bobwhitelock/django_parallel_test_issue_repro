
from unittest.runner import TextTestRunner, TextTestResult

from django.test.runner import DiscoverRunner


class CustomResult(TextTestResult):

    def startTest(self, test):
        print(f"startTest called for {test}")
        super().startTest(test)


class CustomRunner(TextTestRunner):
    resultclass = CustomResult


class CustomDjangoRunner(DiscoverRunner):
    test_runner = CustomRunner
