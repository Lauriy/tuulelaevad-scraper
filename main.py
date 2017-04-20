import requests, bs4

id = 102300
extracted_date = None
extracted_time = None

while extracted_date != '<span class="grid12 ferryDate">K 22.06.2016</span>':
    response = requests.get('http://www.tuulelaevad.ee/index.php?task=step_2&option=com_tuulelaevad_shop&Itemid=23&lang=et&single_trip_id=%s' % id)
    soup = bs4.BeautifulSoup(response.text)
    try:
        extracted_date = soup.select('.ferryDate')[0]
        extracted_time = soup.select('.ferryTime')[0]
    except IndexError:
        pass
    print id
    print extracted_date
    print extracted_time
    id += 1
