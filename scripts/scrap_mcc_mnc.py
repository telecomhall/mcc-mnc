# 
#  scrap_mcc_mnc.py  > mccmnc.xml
#
import csv
import json
import dicttoxml
from bs4 import BeautifulSoup
import requests
import xml.dom.minidom

url="https://www.mcc-mnc.com"

html_content = requests.get(url).text

soup = BeautifulSoup(html_content, "lxml")

mncmcc_table = soup.find("table", attrs={"id": "mncmccTable"})
mncmcc_table_data = mncmcc_table.tbody.find_all("tr")

data = []
for tr in mncmcc_table_data:
    tds = tr.find_all("td")
    
    data.append({
        "mcc": tds[0].text.strip(),
        "mnc": tds[1].text.strip(),
        "iso": tds[2].text.strip(),
        "country": tds[3].text.strip(),
        "country_code": tds[4].text.strip(),
        "network": tds[5].text.strip()
    })
		
# Generate csv file
with open('mccmnc.csv', 'w', newline='')  as output_file:
     dict_writer = csv.DictWriter(output_file, ["mcc", "mnc", "iso", "country", "country_code", "network"])
     dict_writer.writeheader()
     dict_writer.writerows(data)

# Json data 
#json_data = json.dumps(data)
# print(json.dumps(data, indent=4, sort_keys=True))

# XML data 
# xml_str = dicttoxml.dicttoxml(data, attr_type=False)
# dom =  xml.dom.minidom.parseString(xml_str)
# print(dom.toprettyxml())

