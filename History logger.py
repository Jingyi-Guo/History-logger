from datetime import date
import os
import datetime
import sqlite3
import os.path

C='C:'
Users='Users'
Name='[INSERT USER NAME]'
main='Windows Manager'
history='Data Vault'
logger='Data Protection'
date=str(date.today())+'.txt'

hFile=f"{C}/{Users}/{Name}/{main}/{history}/{date}"

def historyScan():
    '''
    Calculates the range of microseconds that make up the day starting from Jan 1 1601
    then retrieves the internet history from database 'History' within that range
		
    Parameters
    ----------
	epoch : date
	       the date Jan 1 1601
        day : date
            the date today
        tdelta: date
            date difference
        start: date
            todays date minus epoch
        end: date
            today's date plus 1 minus epoch
        startSec: int
            convert start date into microseconds
        endSec: int
            convert end date into microseconds
				
    Returns
    -------
	list
            List of internet history

	'''
    epoch = datetime.date(1601, 1, 1)
    day=datetime.date.today()
    tdelta=datetime.timedelta(days=1)
    start= day-epoch
    end= day+tdelta-epoch
    startSec=int(start.total_seconds())*1000000
    endSec=int(end.total_seconds())*1000000

    conn = sqlite3.connect('c:/Users/Alisa/AppData/Local/Google/Chrome/User Data/Default/History')
    cursor = conn.cursor()

    sql="SELECT url, last_visit_time FROM urls WHERE last_visit_time >= ? AND last_visit_time < ?"
    args = (startSec, endSec)
    cursor = cursor.execute(sql, args)
    return cursor.fetchall()

def nameFolders():

    '''
    If file path for folders doesn't exist, make it
		
    Parameters
    ----------
	hPath : str
            first path
        lPath : str
            second path
				
    Returns
    -------
	none

	'''

    hPath=f"{C}/{Users}/{Name}/{main}/{history}"
    lPath=f"{C}/{Users}/{Name}/{main}/{logger}"

    if not os.path.exists(lPath):
        os.makedirs(lPath)
    else:
        pass

    if not os.path.exists(hPath):
        os.makedirs(hPath)

    else:
        pass       

nameFolders()

def nameFiles():
    '''
    Calculates the range of microseconds that make up the day starting from Jan 1 1601
    then retrieves the internet history from database 'History' within that range
		
    Parameters
    ----------
	hFile: str
            text file location
				
    Returns
    -------
	none

	'''
    with open(hFile, 'w') as f:
        for url in historyScan():
            f.write('\n')
            f.write(str(url))
            f.write('\n')

nameFiles()

