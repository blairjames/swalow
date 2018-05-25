#!/usr/bin/env python3

            ###############
              S.W.A.L.O.W 
            ###############
       
   # Simple Web App Load Overload Weapon #
# Test HTTP/s load handling capacity of your web application #
# This tool is only to be used to test your own web application #
# Set number of request senders in "how_many_processes" variable.
# Set URL of site in "url" variable

import requests
import multiprocessing

#SET YOUR OPTIONS HERE#
url: str = "https://'your_URL_here'"
how_many_processes: int = 900

def sendit(x: int):
    '''
    Send requests forever or until stopped manually
    '''
    while True:
        try:
            requests.get(url)
        except Exception as e:
            pass

def go():
    gen = ([x] for x in range(how_many_processes))
    with multiprocessing.Pool(how_many_processes) as pool:
        pool.map(sendit, gen)

if __name__ == '__main__':
    go()
