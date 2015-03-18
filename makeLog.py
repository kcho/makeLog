#!/ccnc_bin/venv/bin/python
import os
import sys
import getpass
import argparse
import datetime
import textwrap
import re

def main(args):
    print 'Directory input : \n\t', args.dirInput
    print 'Log creation date : \n\t', args.date
    print 'Directory location : \n\t', args.loc
    print 'Directory name : \n\t', args.dirName
    print 'Log created / edited by : \n\t', args.user
    print 'Note by user : \n\t', args.extra

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
            {codeName} : Makes or appends various information to a 'log.txt'
            ====================
            eg) {codeName} -dirName --dir /Users/kevin/NOR04_CKI
            eg) {codeName} -n -l
            '''.format(codeName=os.path.basename(__file__))))

    parser.add_argument(
        '-i', '--dirInput',
        help='Saves current directory name to log',
        default=os.getcwd())

    parser.add_argument(
        '-n', '--dirName',
        help='Saves current directory name to log',
        default=os.path.basename(os.getcwd()))

    parser.add_argument(
        '-l', '--loc',
        help='Saves directory location to log',
        default=os.getcwd())

    parser.add_argument(
        '-u', '--user',
        action='store_true',
        help='Saves user name to the log',
        default=getpass.getuser())

    parser.add_argument(
        '-d', '--date',
        action='store_true',
        help='Saves the date of log creation to the log',
        default=datetime.date.today())

    parser.add_argument(
        '-e', '--extra',
        help='Saves the date of log creation to the log',
        )

    args = parser.parse_args()

    if args.dirInput != os.getcwd():
        args.dirName = os.path.basename(args.dirInput)
        args.loc = os.path.abspath(args.dirInput)

    main(args)
