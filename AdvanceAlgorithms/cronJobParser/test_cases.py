import sys
import unittest
from cronJobParser import CronJobParser, InvalidValuesError
from io import StringIO

class TestCronJobParser(unittest.TestCase):

    def test_parse_cron_job(self):
        cron = CronJobParser("*/15 0 1,15 * 1-5 /usr/bin/find")
        result = cron.parseCron()
        self.assertEqual(cron.minutes, "minute       0 15 30 45")
        self.assertEqual(cron.hours, "hour         0")
        self.assertEqual(cron.days, "day of month 1 15")
        self.assertEqual(cron.months, "month        1 2 3 4 5 6 7 8 9 10 11 12")
        self.assertEqual(cron.weekdays, "day of week  1 2 3 4 5")
        self.assertEqual(cron.command, "command      /usr/bin/find")

    def test_parse_cron_job_failure(self):
        cron = CronJobParser("*/15 32 1,15 * 1-5 /usr/bin/find")
        expected_error_message = "Invalid: Cronjobs for hour have to be between 0 and 24\n"
        captured_output = StringIO()
        sys.stdout = captured_output
        with self.assertRaises(SystemExit):
            cron.parseCron()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_error_message)

    def test_parse_cron_job_failure_range(self):
        cron = CronJobParser("*/15 31 1,15 * 1-8 /usr/bin/find")
        expected_error_message = "Invalid: Cronjobs for day of week have to be between 0 and 7\n"
        captured_output = StringIO()
        sys.stdout = captured_output
        with self.assertRaises(SystemExit):
            cron.parseCron()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_error_message)

    def test_parse_cron_job_failure_slash(self):
        cron = CronJobParser("62/5 0 1,15 * 1-5 /usr/bin/find")
        expected_error_message = "Invalid: Cronjobs for minute have to be between 0 and 60\n"
        captured_output = StringIO()
        sys.stdout = captured_output
        with self.assertRaises(SystemExit):
            cron.parseCron()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_error_message)

    def test_parseString_minute(self):
        cron = CronJobParser("* * * * * /usr/bin/find")
        result = cron.parseString("minute", "*", 0, 60)
        self.assertEqual(result, "minute       0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59")

    def test_parseString_hour(self):
        cron = CronJobParser("* * * * * /usr/bin/find")
        result = cron.parseString("hour", "*", 0, 24)
        self.assertEqual(result, "hour         0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23")

    def test_parseString_day_of_month(self):
        cron = CronJobParser("* * * * * /usr/bin/find")
        result = cron.parseString("day of month", "*", 1, 32)
        self.assertEqual(result, "day of month 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31")

    def test_parseString_month(self):
        cron = CronJobParser("* * * * * /usr/bin/find")
        result = cron.parseString("month", "*", 1, 13)
        self.assertEqual(result, "month        1 2 3 4 5 6 7 8 9 10 11 12")

    def test_parseString_day_of_week(self):
        cron = CronJobParser("* * * * * /usr/bin/find")
        result = cron.parseString("day of week", "*", 0, 7)
        self.assertEqual(result, "day of week  0 1 2 3 4 5 6")

    # def test_parseString_invalid_values(self):
    #     cron = CronJobParser("* * * * * /usr/bin/find")
    #     with self.assertRaises(InvalidValuesError):
    #         cron.parseString("minute", "60", 0, 61)

if __name__ == "__main__":
    unittest.main()
