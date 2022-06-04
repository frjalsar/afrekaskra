# Units
Units_symbol = {1: 'm', 2: 's', 3: 'mm:ss,dd', 4: 'hh:mm:ss,dd', 5: 'stig', 6: 'stig'}

# stuff
import re
prog_time = re.compile('^(?:(?:([01]?\d|2[0-3]):)?([0-5]?\d):)?(\d+\.?\d*)?$') # Notum regex

#-------------------------------------------------------------------------------
# Fall sem breytir streng með árangri yfir í rauntölu
# '65.76' -> 65.76
# ''      -> NaN
# 'ABCD'  -> NaN
# Ef strengurinn er tími á forminu HH:MM:SS.FF þá er honum breytt yfir í sek
# '02:43.45' -> 2*60 + 43.45 = 163.45
# '01:02.45' -> 1*60*60 + 2*60 + 43.45 = 3763.45
def results_to_float_old(in_str):
    #prog_time = re.compile('^(?:(?:([01]?\d|2[0-3]):)?([0-5]?\d):)?(\d+\.?\d*)?$') # Notum regex
    m = prog_time.match(str(in_str).replace(',', '.'))
    if (m): # Athuga hvort við fengum match

        if (m.group(1) is None and m.group(2) is None and m.group(3) is None):
            return np.nan # Eitthvað skrítið í gangi eða tómur strengur skila NaN

        time_sec = 0.0 # Breytum yfir í sek ef þetta er tími
        if (m.group(1) is not None):
            time_sec = float(m.group(1))*3600.0 # 60*60 = 3600
        if (m.group(2) is not None):
            time_sec = time_sec + float(m.group(2))*60.0
        if (m.group(3) is not None):
            time_sec = time_sec + float(m.group(3))

        return time_sec
    else:
        print('String er')
        print(in_str)
        print('Error')
        raise ValueError()
        return None

def results_to_float(in_str):
    # Skiptum kommu út fyrir punkt. Sumir árangrar eru með kommu en aðrir með punkt.
    split = str(in_str).replace(',', '.').split(' ')[0].split('.') # Splitta eftir kommu .dd. 
       # Splittum líka á bili ' ', því SQL procedure var breytt til að innihalda texta á eftir árangri
    hh = 0
    mm = 0
    ss = 0
    dd = 0
    
    if (len(split) == 2): # hh:mm:ss,dd eða mm:ss,dd eða ss,dd. Sem sagt eitthvað eftir kommu, ,dd
        if (len(split[1]) == 1): # Ein aukastafur eftir kommu þýðir handtímataka
            dd = float(split[1])/10 # Handtími ,d
        else:
            dd = float(split[1])/100 # Rafmagnstími ,dd
    
    split = split[0].split(':')
    if (len(split) == 3): # hh:mm:ss
        hh = float(split[0])
        mm = float(split[1])
        ss = float(split[2])
    elif (len(split) == 2): # mm:ss
        mm = float(split[0])
        ss = float(split[1])
    elif (len(split) == 1): # ss
        try:
            ss = float(split[0])
        except ValueError: # Some results are stored as DNF.
            ss = -1.0
        
    time_sec = hh*3600 + mm*60 + ss + dd
    # print('')
    # print('Formating string to float')
    # print('Input: ' + in_str)
    # print(hh)
    # print(mm)
    # print(ss)
    # print(dd)
    # print(time_sec)
    # print('Done')
    # print('')
    return time_sec

#Units_symbol = {1: 'm', 2: 's', 3: 'mm:ss,dd', 4: 'hh:mm:ss,dd', 5: 'stig', 6: 'stig'}
def results_to_str(in_float, Units, ElectricTiming):
    if (in_float < 0.0): # Engin árangur
        return ''

    if (Units == 1): # m
        return '{:.2f}'.format(in_float)

    elif (Units == 2): # s
        if (ElectricTiming == True):
            return '{:05.2f}'.format(in_float)
        else:
            return '{:04.1f}'.format(in_float) + 'h'

    elif (Units == 3): # mm:ss,dd
        ss = in_float
        mm = int(ss // 60)
        ss = ss % 60

        if (ElectricTiming == True):
            return '{:02d}:{:05.2f}'.format(mm, ss)
        else:
            return '{:02d}:{:04.1f}'.format(mm, ss) + 'h'

    elif (Units == 4): # hh:mm:ss,dd
        ss = in_float
        hh = int(ss // (60*60))
        ss = ss % (60*60)
        mm = int(ss // 60)
        ss = ss % 60

        if (ElectricTiming == True):
            return '{:02d}:{:02d}:{:05.2f}'.format(hh, mm, ss)
        else:
            return '{:02d}:{:02d}:{:04.1f}'.format(hh, mm, ss) + 'h'

    elif (Units == 5): # points
        return '{:.0f}'.format(in_float)

    elif (Units == 6): # points
        return '{:.0f}'.format(in_float)
        
    else:
        raise ValueError

def wind_to_str(in_float, inout=None, hasWind=True):
    if (inout == 1):
        return ''
    else:
        if (hasWind == True):
            return '{:+.1f}'.format(in_float)
        else:
            return ''