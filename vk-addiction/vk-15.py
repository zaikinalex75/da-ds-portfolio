import time
import datetime
import sys
import requests
import re

# --------------------------------------------------------------------
def execute():
# --------------------------------------------------------------------
    ON_SUMB = '*'
    MOBILE_KEY = 'svgIcon-online_mobile'
    dt = datetime.datetime.now()
    on, lmin, message, http = '', '', '', ''

    re_last_activity = re.compile(
        r'<span\s[^>]*class\s*=\s*["'']pp_last_activity_text["''][^>]*>'
        r'(?P<text>.*?)<', re.IGNORECASE)
    re_min = re.compile(
        r'заходила?\s*(?P<min>\d+)\s*минут', re.IGNORECASE)

    try:
        url = 'https://vk.com/' + sys.argv[1]
        http = requests.get(url).text
        #with open('xxx-was-7-min.txt') as f:
        #    http = f.read()
        search_result = re_last_activity.search(http)
        last_activity = search_result.group('text').strip().lower()
        if last_activity == 'online':
            on, lmin = ON_SUMB, '0'
        elif last_activity == 'заходил только что':
            on, lmin = ON_SUMB, '0'
        elif last_activity == 'заходил минуту назад':
            on, lmin = ON_SUMB, '1'
        elif last_activity == 'заходил две минуты назад':
            on, lmin = ON_SUMB, '2'
        elif last_activity == 'заходил три минуты назад':
            on, lmin = ON_SUMB, '3'
        else:
            search_result = re_min.search(last_activity)
            if search_result:
                lmin = search_result.group('min')
                if int(lmin) < 14:
                    on = ON_SUMB 
            else:
                message = last_activity
        device = 'm' if MOBILE_KEY in http else '-'
        message = '[' + device + '] '  + message
    except:
        message = 'EXCEPTION! ' + str(sys.exc_info()[1])
    finally:
        print('{}\t{}\t{}\t{}'.format(dt.strftime('%d.%m.%Y %H:%M'), 
            on, lmin, message))
        #print()
        #print(http)
        
# --------------------------------------------------------------------
# MAIN 15 MIN LOOP
# --------------------------------------------------------------------
#execute()
while True:
    time.sleep(6)
    dt = datetime.datetime.now()
    if ((dt.minute % 15) == 0) and ((dt.hour <= 1) or (dt.hour >= 8)):
        execute()
        # спим 13 мин, а не 15, чтобы иметь пару мин. на таймаут сети
        time.sleep(13*60) 
