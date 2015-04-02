from datetime import date

head = '--------------------\n\
MO TU WE TH FR SA SU\n\
--------------------\n'

def create_calendar_page(month=None,year=None):
    str_cal = istr = '' 
    nmonth = nyear = 0
    if year == None:
        year = date.today().year
    if month == None:
        month = date.today().month   
    day_ord = date(year,month,1).weekday()
    istr = day_ord*'   ' + str(date(year,month,1).day).zfill(2)+' '
    if month == 12:
        nmonth = 1
        nyear = year + 1
    else:
        nmonth = month + 1
        nyear = year
    dim = (date(nyear,nmonth,1) - date(year,month,1)).days   
    for i in range(2,dim+1):
        if len(istr) == 21:
            istr = istr.rstrip()
            str_cal += istr + '\n'
            istr = ''
        day = str(date(year,month,i).day).zfill(2)
        istr += day + ' '
    str_cal = (str_cal + istr).rstrip()    
    return (head + str_cal)    
    
print(create_calendar_page(12,2019))   
