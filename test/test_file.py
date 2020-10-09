import pytest


class Testfile:
    def test_file1(self):
        print('Hey')
    @pytest.mark.xfail
    def test_file2(self):
        print('Hello')