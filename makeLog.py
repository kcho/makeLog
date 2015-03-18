#!/ccnc_bin/venv/bin/python
import os
import sys
import getpass
import argparse
import datetime
import textwrap
import re
import socket

def main(args):
    args.dirInput = os.path.abspath(args.dirInput)

    if socket.gethostname().find('.')>=0:
        hostname=socket.gethostname()
    else:
        hostname=socket.gethostbyaddr(socket.gethostname())[0]

    content = '{date} by {user}\n\
{hostname}\n\
{line}\n\
{dirLoc}\n\
{basename}\n\
{extra}\n'.format(date = args.date,
                user = args.user,
                line = '='*60,
                dirLoc = os.path.dirname(args.dirInput),
                basename = os.path.basename(args.dirInput),
                hostname = hostname,
                extra = args.extra)

    #print content
    
    # if there is log
    logLoc = os.path.join(args.dirInput,'log.txt')
    if os.path.isfile(logLoc):
        print 'There is log... appending\n'
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

    if args.extra == None:
        args.extra = ''

    main(args)
