import scrapy
from scrapy_selenium import SeleniumRequest
import json
import os

# Path to the file where blacklisted IPs will be stored
BLACKLIST_FILE = 'blacklisted_ips.json'

# Function to load blacklisted IPs from the file
def load_blacklisted_ips():
    if os.path.exists(BLACKLIST_FILE):
        with open(BLACKLIST_FILE, 'r') as f:
            return json.load(f)
    return []

# Function to save blacklisted IPs to the file
def save_blacklisted_ips(ips):
    with open(BLACKLIST_FILE, 'w') as f:
        json.dump(ips, f)

class MyIPSpider(scrapy.Spider):
    name = "myip_dynamic"
    start_urls = [
        "https://www.projecthoneypot.org/list_of_ips.php",
    ]

    def start_requests(self):
        print("CRAWLING STARTED")
        for url in self.start_urls:
            yield SeleniumRequest(url=url, callback=self.parse)

    def parse(self, response):
        # Locate the rows in the table
        rows = response.xpath('//div[contains(@class, "contain")]/table/tr')

        # Load existing blacklisted IPs
        blacklisted_ips = load_blacklisted_ips()

        for row in rows:
            # Extract the text of the second <a> inside the first <td>
            ip = row.xpath('.//td[1]/a[2]/text()').get()  # Getting the IP
            next_link = row.xpath('.//td[1]/a[2]/@href').get()  # Getting the href
            
            if ip and ip not in blacklisted_ips:
                # If the IP is not already blacklisted, add it to the list
                blacklisted_ips.append(ip)
                # Save the updated blacklisted IPs back to the file
                save_blacklisted_ips(blacklisted_ips)
                
                yield {
                    'ip': ip,
                    'next_link': response.urljoin(next_link),  # Full URL
                }

                # Optionally follow the link in the href for further crawling
                # yield SeleniumRequest(url=response.urljoin(next_link), callback=self.parse)
