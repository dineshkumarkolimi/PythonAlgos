CronJobParser:

To Run a Cron Job: `~$ your-program "*/15 0 1,15 * 1-5 /usr/bin/find"`

What can not be given: negative values are not allowed and values can not be out of range for each field

range of values: 
    minutes: 0-59
    hours: 0-23
    days: 1-31
    months: 1-12 (JAN-DEC is not supported)
    day of week: 0-6 (SUN-FRI is not supported)

Output Format: 
        `minute 0 15 30 45
        hour 0
        day of month 1 15
        month 1 2 3 4 5 6 7 8 9 10 11 12
        day of week 1 2 3 4 5
        command /usr/bin/find`

To run test cases: `python3 test_cases.py`

output format:
python3 test_cases.py
.........
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK

