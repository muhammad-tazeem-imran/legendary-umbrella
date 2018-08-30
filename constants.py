
MONTH_NAMES = [
    'January','February','March',
    'April','May','June',
    'July','August','September',
    'October','November','Decemeber'
    ]
    
ERROR_MSG = '   Missing command line Arguments \n \
    Run Command \n \
        [python version] weatherman.py [dir] [option] [details] \n\n \
        dir\n \
            Path to the weather files\n \
        option\n \
            -e for yearly report\n \
            -a for monthly report\n \
            -c for monthly graph\n \
        details\n \
            year[/month] (month is not required for yearly report)\n '

ERROR_MSG_2 = 'One or more invalid command line arguments'

COLOR_BLUE = '\033[1;34;48m'
COLOR_RED = '\033[1;31;48m'
COLOR_NORM = '\033[0m'