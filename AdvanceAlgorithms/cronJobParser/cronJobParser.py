"""_summary_
    The cron string will be passed to your application as a single argument.
    ~$ your-program "*/15 0 1,15 * 1-5 /usr/bin/find"

    Returns: display the results in following format
        minute 0 15 30 45
        hour 0
        day of month 1 15
        month 1 2 3 4 5 6 7 8 9 10 11 12
        day of week 1 2 3 4 5
        command /usr/bin/find
"""

import sys


"""
    Raises:
        InvalidValuesError: When ever integers are passed are out of range.

    Returns:
        _type_: string describing error type
"""
class InvalidValuesError(Exception):
    def __init__(self, message="Default error message"):
        self.message = message
        super().__init__(self.message)


"""
    This class implements the conversion of cron parameters to values
"""
class CronJobParser(object):

    def __init__(self, cron_string):
        self.cron_string = cron_string
        self.minutes = None
        self.hours = None
        self.days = None
        self.months = None
        self.weekdays = None
        self.command = None

    """
        This method is called by cron when running a command against the command line and returns 
        the string representation of cron job for minutes, seconds, days, month, and day of week
    """
    def parseString(self, field, value, start=None, end=None):
        try: 
            # Check if value is a range of numbers
            if '-' in value:
                temp_start, temp_end = map(int, value.split('-'))
                if temp_start < start or temp_end > end or temp_end < start or temp_start > end:
                    raise InvalidValuesError(f'Invalid: Cronjobs for {field} have to be between {start} and {end}')
                result = [i for i in range(temp_start, temp_end+1)]
            # Check if value is incremented on step wise manner        
            elif '/' in value:
                temp_start, step = value.split('/')
                if temp_start != '*' and (int(temp_start) < start or int(temp_start) > end):
                    raise InvalidValuesError(f'Invalid: Cronjobs for {field} have to be between {start} and {end}')
                start = start if temp_start=='*' else int(temp_start)
                result = [i for i in range(start, end, int(step))]
            # Check if list of values are provided
            elif ',' in value:
                result = map(int, value.split(','))
            # Check if it contains all possible values for that field
            elif '*' in value:
                result = [i for i in range(start, end)]
                if not all(start <= x <= end for x in result):
                    raise InvalidValuesError(f'Invalid: Cronjobs for {field} have to be between {start} and {end}')
            # Case when single value is provided
            else:
                if  int(value) < start or int(value) > end:
                    raise InvalidValuesError(f'Invalid: Cronjobs for {field} have to be between {start} and {end}')
                result = [value]
            return field + ' '*(13-len(field)) + ' '.join(map(str, result))
        except (ValueError, TypeError, IndexError, AttributeError) as e:
            print('ERROR: Invalid Format: ' + str(e))
            sys.exit(1)
        except InvalidValuesError as e:
            print(e)
            sys.exit(1)

    """
        This method calls parseString method for various formats and adds 
        them in the appropriate format to class variables
    """
    def parseCron(self):
        cronItems = self.cron_string.split(' ')
        self.command = 'command      ' + cronItems[-1]
        self.weekdays = self.parseString("day of week", cronItems[4], 0, 7)
        self.months = self.parseString("month", cronItems[3], 1, 13)
        # Handling February scenario
        if self.months.split(' ')[-1] == '2':
            self.days = self.parseString("day of month", cronItems[2], 1, 29)
        else:
            self.days = self.parseString("day of month", cronItems[2], 1, 32)
        self.hours = self.parseString("hour", cronItems[1],0,24)
        self.minutes = self.parseString("minute", cronItems[0],0,60)

    """
        Prints all the cron items to the console
    """
    def display(self):
        print(self.minutes + "\n" + self.hours + "\n" + self.days + "\n" + self.months + 
              "\n" + self.weekdays + "\n" + self.command)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 cronJobParser.py 'cron_string'")
        sys.exit(1)
    # Fetching cron string from the arguments provided
    cronString = sys.argv[1]
    # Creating a new cronJobParser object
    cron = CronJobParser(cronString)
    cron.parseCron()
    cron.display()