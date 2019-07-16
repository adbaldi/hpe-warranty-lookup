#!/bin/env python

import sys
import http.client
import urllib.parse
from bs4 import BeautifulSoup

def get_warranty_HTML(serial):
    params = urllib.parse.urlencode({'rows[0].item.serialNumber': serial})
    headers = {"Content-type": "application/x-www-form-urlencoded"}

    conn = http.client.HTTPSConnection("support.hpe.com")
    conn.request("POST", "/hpsc/wc/public/find", params, headers)
    response = conn.getresponse()
    
    if response.status != 200:
        sys.exit(response.reason)

    data = response.read()
    return data

def extract_warranty_info(html):
    active_warranties = []
    soup = BeautifulSoup(html, 'html.parser')
    active = soup.find_all("td", attrs={"style": 'color: Green'}, string="Active")

    for td in active:
        warranty = {
            "service_type" : td.previous_sibling.previous_sibling.previous_sibling.get_text(strip=True),
            "start_date"   : td.previous_sibling.previous_sibling.string,
            "end_date"     : td.previous_sibling.string
        }
        active_warranties.append(warranty)

    return active_warranties


def main():
        cnt = 0
        count_lines = len(open('serials.txt').readlines())
        print ('\n%s serials to check \n-----------------------\n' % (count_lines))
        for line in open('serials.txt'):
          print('%s/%s Searching for %s' % (cnt + 1, count_lines, line.rstrip()))
          warranty_html = get_warranty_HTML(line)
          print('Checked!!')
          print('----------------------------\n')
          f = open("checked.txt","a")
          for i in range(1):
            f.write("%s\n %s \n\n" % (line.rstrip(), extract_warranty_info(warranty_html)))
          f.close()
          cnt += 1
        print('Saved details to checked.txt.\n\nFinished...!!! \n')

if __name__ == '__main__':
    main()
