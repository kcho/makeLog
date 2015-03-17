#!/ccnc_bin/venv/bin/python
import os
import sys
import re

def main():
    print 'haha'

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
            {codeName} : Makes or appends various information to a 'log.txt'
            ====================
            eg) {codeName} -dirName --dir /Users/kevin/NOR04_CKI
            '''.format(codeName=os.path.basename(__file__))))

    parser.add_argument(
        '-dirName', '--directoryName',
        help='Saves current directory name to log',
        default=os.path.basename(os.getcwd()))

    parser.add_argument(
        '-loc', '--location',
        help='Saves directory location to log',
        default=False)

    parser.add_argument(
        '-u', '--user',
        help='Saves user name to the log',
        default=True)

    parser.add_argument(
        '-d', '--date',
        help='Saves the date of log creation to the log',
        default=True)

    args = parser.parse_args()

    main(args)
