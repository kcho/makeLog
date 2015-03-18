#!/ccnc_bin/venv/bin/python
import os
import sys
import getpass
import argparse
import datetime
import textwrap
import re

def main(args):

    content = '{date}   by {user}\n\
{line}\n\
{dirInput}\n\
{basename}\n\
{extra}'.format(date = args.date,
                user = args.user,
                line = '='*25,
                dirInput = args.dirInput,
                basename = args.dirName,
                extra = args.extra)

    #print content
    
    # if there is log
    logLoc = os.path.join(args.dirInput,'log.txt')
    if os.path.isfile(logLoc):
        print 'There is log... appending \n{0}'.format(content)
        with open(logLoc,'a') as logFile:
            logFile.write(content)
    else:
        print 'There is no log... creating log.txt'
        print content
        with open(logLoc,'w') as logFile:
            logFile.write(content)



    


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
        '-l', '--dirLocation',
        help='Saves current directory name to log',
        default=os.path.dirname(os.getcwd()))

    parser.add_argument(
        '-n', '--dirName',
        help='Saves current directory name to log',
        default=os.path.basename(os.getcwd()))

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

    if args.dirInput != os.path.dirname(os.getcwd()):
        args.dirName = os.path.basename(args.dirInput)

    main(args)
