from flask import Flask, jsonify
from getip import getip
from web_crawler import MyIPSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import threading
import json
import os

app = Flask(__name__)

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

@app.route('/')
def start():
    return 'Hello world'

# @app.route('/getips')
# def getip():
#     ip_set = getip()  # Get IPs from the network
#     return jsonify(ip_set)

@app.route('/check_threats')
def check_threats():
    ip_set = getip()  # Get IPs from the network
    process = CrawlerProcess(get_project_settings())
    
    # Define a function to run the spider
    def crawl():
        process.crawl(MyIPSpider)
        process.start()
    
    # Run the spider in a separate thread
    thread_crawl = threading.Thread(target=crawl)
    thread_crawl.start()

    # Load existing blacklisted IPs from the file
    blacklisted_ips = load_blacklisted_ips()

    black_ip = []
    for ip in ip_set:
        if ip in blacklisted_ips:
            black_ip.append(ip)
    
    if black_ip:
        return jsonify(black_ip)
    else:
        return jsonify({"msg":"All done and safe"})

if __name__ == '__main__':
    # Ensure the blacklisted IPs file exists
    if not os.path.exists(BLACKLIST_FILE):
        save_blacklisted_ips([])  # Initialize with an empty list

    # Run the Flask app
    app.run(debug=True, port=5001)
