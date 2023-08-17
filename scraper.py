"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Michael Čermák
email: michael.cermak92@gmail.com
discord: MichaelCe#8181
"""

import requests
import csv
import traceback
import sys
import time

from bs4 import BeautifulSoup

def get_soup(url):
    server_response = requests.get(url)
    soup = BeautifulSoup(server_response.text, "html.parser")
    return soup

def urls_fill(url):
    """
    Creates the list of url of all cities from the entry URL
    """
    table_tag = get_soup(url).find_all("table", {"class": "table"})
    urls = []
    for table in table_tag:
        tr_tag = table.find_all("tr")
        for tr in tr_tag[2:]:
            td_tag = tr.find_all("td", {"class": "cislo"})
            for td in td_tag:
                ahref = td.find("a").get("href")
                urls.append("https://volby.cz/pls/ps2017nss/" + ahref)
    return urls

def get_location(url):
    """
    Gets a single city
    """
    h3_tag = get_soup(url).find_all("h3")
    return (h3_tag[2].get_text())[7:-1:]

def get_party(url):
    
    table_tag = get_soup(url).find_all("table", {"class": "table"})
    for table in table_tag[1:]:
        tr_tag = table.find_all("tr")
        break

    for tr in tr_tag[2:]:
        td_tag = tr.find_all("td", {"class": "overflow_name"})
        break
    return td_tag[0].get_text()

def get_party_votes(url):
    table_tag = get_soup(url).find_all("table", {"class": "table"})
    for table in table_tag[1:]:
        tr_tag = table.find_all("tr")
        break

    for tr in tr_tag[2:]:
        td_tag = tr.find_all("td", {"class": "cislo"})
        break          
    return td_tag[1].get_text()      
        
def parties_list(url):
    """
    Get list of political parties for first line in csv
    """
    table_tag = get_soup(url).find_all("table", {"class": "table"})
    parties = []
    for table in table_tag[1:]:
        tr_tag = table.find_all("tr")
        for tr in tr_tag[2:]:
            td_tag = tr.find_all("td", {"class": "overflow_name"})
            for td in td_tag:            
                parties.append(td_tag[0].get_text())
    return parties

def parties_votes_list(url):
    """
    Get list of votes for all political parties for other than first line in csv
    """
    table_tag = get_soup(url).find_all("table", {"class": "table"})
    parties_votes = []
    for table in table_tag[1:]:
        tr_tag = table.find_all("tr")
        for tr in tr_tag[2:]:
            td_tag = tr.find_all("td", {"class": "cislo"})
            for td in td_tag:            
                parties_votes.append(td_tag[1].get_text())
                break
    return parties_votes

def overall_data(url):
    """
    Gets the list for entire row in CSV
    """
    table_tag = get_soup(url).find_all("table", {"class": "table"})
    for table in table_tag:
        tr_tag = table.find_all("tr")
        break

    for tr in tr_tag:
        td_tag = tr.find_all("td", {"class": "cislo"})

    code = url[62:68]
    location = get_location(url)
    votes = parties_votes_list(url)
    list_complete_data = [code, location, td_tag[3].get_text(),
                          td_tag[4].get_text(), td_tag[7].get_text()]
    list_complete_data.extend(votes)
    
    return list_complete_data

def data_into_csv(data: list, file_name: str) -> str:
    """
    Enters the data into file
    """
    try:
        csv_file = open(file_name, 'a', newline='', encoding="utf-8")
    # Step 4: Using csv.writer to write the list to the CSV file
        writer = csv.writer(csv_file)
        writer.writerow(data) # Use writerow for single list

    except FileExistsError:
        return traceback.format_exc()
    except IndexError:
        return traceback.format_exc()

    finally:
        csv_file.close()

def main():
    arg_url = sys.argv[1]
    arg_filename = sys.argv[2]

    print("Getting data from URL:" + arg_url)

    urls_of_cities = urls_fill(arg_url)
    first_line_index = True
    for city in urls_of_cities:
        
        if first_line_index is True:
            first_line_csv = ["Code", "Location", "Registered", "Envelopes", "Valid"]
            first_line_csv.extend(parties_list(city))
            data_into_csv(first_line_csv, arg_filename)
            first_line_index = False

        overall_data(city)
        data_into_csv(overall_data(city), arg_filename)
    
    print("Data has been saved to " + arg_filename)

if __name__ == "__main__":
    
    try:
        start_time = time.time()
        main()
        print("Program " + sys.argv[0] + " ended in %s seconds" % (time.time() - start_time))

    except IndexError:
        print("Missing argument/s")
    except:
        print("Wrong input!!!")
