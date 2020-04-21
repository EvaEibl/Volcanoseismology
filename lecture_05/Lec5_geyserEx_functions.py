# Lecture 5: Snuffler exercise functions 
# 
# author: Eva Eibl eva.eibl@uni-potsdam.de
# SS 2019: Module MGPW02
# -------------------------------

import matplotlib.pyplot as plt

def read_snuffler_marker(filen, length=1, nojul=0):
    """
    Helper function to read snuffler marker.
    :type filen: string
    :param filen: path to snuffler marker file 
    :type length: 0 or 1         
    :param length: indicates whether marker file has 
                   4 columns [key 0] (start date, start time, class, station) or 
                   6 columns [key 1] (start date, start time, end date, end time, class, station)
    :type nojul: 0 or 1
    :param nojul: 0 if date returned in julday, 1 if returned in year, month...

    :return: time, event class.
    """
    ## -- read in lines 
    f = open (filen, 'r')
    lines = []
    for line in f : 
        li = line.strip()
        if not li.startswith("#"): # ignore lines that start with #
            lines.append(li)
        #end
    #end
    f.close()

    ## -- read certain values from lines
    date1 = []
    tim1 = []
    date2 = []
    tim2 = []
    evclass1 = []
    evclass2 = []
    for i in range(len(lines)):
        temp = lines[i]
        if length==1:
            if len(temp.split())!=4:
                date1.append(temp.split()[0])
                tim1.append(temp.split()[1])
                date2.append(temp.split()[2])
                tim2.append(temp.split()[3])
                evclass2.append(float(temp.split()[4]))
            #end
        else:
            date1.append(temp.split()[0])
            tim1.append(temp.split()[1])
            evclass1.append(float(temp.split()[2]))
        #end
    #end

    ## -- extract year, day, hour etc. from date, time
    year1 = []
    mon1 = []
    day1 = []
    hour1 = []
    minu1 = []
    sec1 = []
    year2 = []
    mon2 = []
    day2 = []
    hour2 = []
    minu2 = []
    sec2 = []
    for i in range(len(date1)):
        year1.append(int(date1[i].split('-')[0]))
        mon1.append(int(date1[i].split('-')[1]))
        day1.append(int(date1[i].split('-')[2]))
        hour1.append(int(tim1[i].split(':')[0]))
        minu1.append(int(tim1[i].split(':')[1]))
        sec1.append(float(tim1[i].split(':')[2]))
    #end
    if length==1:
        for i in range(len(date2)):
            year2.append(int(date2[i].split('-')[0]))
            mon2.append(int(date2[i].split('-')[1]))
            day2.append(int(date2[i].split('-')[2]))
            hour2.append(int(tim2[i].split(':')[0]))
            minu2.append(int(tim2[i].split(':')[1]))
            sec2.append(float(tim2[i].split(':')[2]))
        #end
    #end
     
    ## -- calculate julday date
    julday1 = convertJulday(year1, mon1, day1, hour1, minu1, sec1)
    julday2 = convertJulday(year2, mon2, day2, hour2, minu2, sec2)

    if length==0:
        if nojul==0:
            return julday1, evclass1
        if nojul==1:
            return year1, mon1, day1, hour1, minu1, sec1, evclass1
        #end
    elif length==1:
        if nojul==0:
            return julday1, julday2, evclass2
        if nojul==1:
            return year1, mon1, day1, hour1, minu1, sec1, year2, mon2, day2, hour2, minu2, sec2, evclass2
        #end
    #end

def convertJulday(year, month, day, hour, minu, second):
  """
  Helper function to convert year, month, day into julday
    :type year: array
    :param year: year of data point
    :type month: array
    :param month: month of data point
    :type day: array
    :param day: day of data point
    :type hour: array
    :param hour: hour of data point
    :type minu: array
    :param minu: minute of data point
    :type second: array
    :param second: second of data point

    :return: julian day 1 column array
  """

  # -- convert to julday
  julday=[]
  for i in range(len(year)):
    if year[i]==2013 or year[i]==2014 or year[i]==2015 or year[i]==2017 or year[i]==2018:
       if month[i]==1:
          julday.append(0+day[i]+hour[i]/24.+minu[i]/(24.*60.)+second[i]/(24.*60.*60.))
       elif month[i]==2:
          julday.append(31+day[i]+hour[i]/24.+minu[i]/(24.*60.)+second[i]/(24.*60.*60.))
       elif month[i]==3:
          julday.append(59+day[i]+hour[i]/24.+minu[i]/(24.*60.)+second[i]/(24.*60.*60.))
       elif month[i]==4:
          julday.append(90+day[i]+hour[i]/24.+minu[i]/(24.*60.)+second[i]/(24.*60.*60.))
       elif month[i]==5:
          julday.append(120+day[i]+hour[i]/24.+minu[i]/(24.*60.)+second[i]/(24.*60.*60.))
       elif month[i]==6:
          julday.append(151+day[i]+hour[i]/24.+minu[i]/(24.*60.)+second[i]/(24.*60.*60.))
       elif month[i]==7:
          julday.append(181+day[i]+hour[i]/24.+minu[i]/(24.*60.)+second[i]/(24.*60.*60.))
       elif month[i]==8:
          julday.append(212+day[i]+hour[i]/24.+minu[i]/(24.*60.)+second[i]/(24.*60.*60.))
       elif month[i]==9:
          julday.append(243+day[i]+hour[i]/24.+minu[i]/(24.*60.)+second[i]/(24.*60.*60.))
       elif month[i]==10:
          julday.append(273+day[i]+hour[i]/24.+minu[i]/(24.*60.)+second[i]/(24.*60.*60.))
       elif month[i]==11:
          julday.append(304+day[i]+hour[i]/24.+minu[i]/(24.*60.)+second[i]/(24.*60.*60.))
       elif month[i]==12:
          julday.append(334+day[i]+hour[i]/24.+minu[i]/(24.*60.)+second[i]/(24.*60.*60.))
       #end
    elif year[i]==2012 or year[i]==2016:
       if month[i]==1:
          julday.append(0+day[i]+hour[i]/24.+minu[i]/(24.*60.)+second[i]/(24.*60.*60.))
       elif month[i]==2:
          julday.append(31+day[i]+hour[i]/24.+minu[i]/(24.*60.)+second[i]/(24.*60.*60.))
       elif month[i]==3:
          julday.append(60+day[i]+hour[i]/24.+minu[i]/(24.*60.)+second[i]/(24.*60.*60.))
       elif month[i]==4:
          julday.append(91+day[i]+hour[i]/24.+minu[i]/(24.*60.)+second[i]/(24.*60.*60.))
       elif month[i]==5:
          julday.append(121+day[i]+hour[i]/24.+minu[i]/(24.*60.)+second[i]/(24.*60.*60.))
       elif month[i]==6:
          julday.append(152+day[i]+hour[i]/24.+minu[i]/(24.*60.)+second[i]/(24.*60.*60.))
       elif month[i]==7:
          julday.append(182+day[i]+hour[i]/24.+minu[i]/(24.*60.)+second[i]/(24.*60.*60.))
       elif month[i]==8:
          julday.append(213+day[i]+hour[i]/24.+minu[i]/(24.*60.)+second[i]/(24.*60.*60.))
       elif month[i]==9:
          julday.append(244+day[i]+hour[i]/24.+minu[i]/(24.*60.)+second[i]/(24.*60.*60.))
       elif month[i]==10:
          julday.append(274+day[i]+hour[i]/24.+minu[i]/(24.*60.)+second[i]/(24.*60.*60.))
       elif month[i]==11:
          julday.append(305+day[i]+hour[i]/24.+minu[i]/(24.*60.)+second[i]/(24.*60.*60.))
       elif month[i]==12:
          julday.append(335+day[i]+hour[i]/24.+minu[i]/(24.*60.)+second[i]/(24.*60.*60.))
       #end
    #end
  #end
  return julday
