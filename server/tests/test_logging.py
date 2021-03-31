import io
from unittest import TestCase
from unittest.mock import patch

from src.utils.logging import with_exception_log


@with_exception_log
def make_exception():
    _ = 0 / 0


class Test(TestCase):

    def test_with_exception_log_rethrows_exception(self):
        self.assertRaises(ZeroDivisionError, make_exception)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_with_exception_log_printed_out(self, mock_stdout):
        try:
            0/0
        except ZeroDivisionError as e:
            try:
                make_exception()
            except Exception as i:
                pass
            self.assertEqual(f"{e.__str__()}\n", mock_stdout.getvalue())
