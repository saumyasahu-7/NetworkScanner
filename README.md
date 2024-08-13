# Network Scanner and Threat Detection

This project is a simple network scanning and threat detection tool. It involves capturing IPs on the network, crawling a blacklist site for malicious IPs, and checking if any IPs on the network are blacklisted.

## Project Structure

- **getip.py**: Captures IPs from the network.
- **web_crawler.py**: Crawls a website for blacklisted IPs.
- **app.py**: Manages the application flow and checks for threats.
- **streamlit_app.py**: Provides a user-friendly interface to interact with the application.

## Components

### 1. `getip.py` - Capturing Network IPs
This script uses the `scapy` library to capture packets on the network and extracts IP addresses. It stores these IPs, which are later used to check against a blacklist.

### 2. `web_crawler.py` - Crawling for Blacklisted IPs
This script uses the `Scrapy` framework along with `scrapy-selenium` to scrape a website for blacklisted IPs. The crawler parses the IP addresses from the site and saves them into a file (`blacklisted_ips.json`).

### 3. `app.py` - Running the Application and Checking for Threats
The main application logic is managed here:
- It calls `getip.py` to get the IPs from the network.
- It then triggers `web_crawler.py` to update the blacklist.
- Finally, it compares the captured IPs with the blacklisted IPs and returns a response indicating if any threats are detected.

### 4. `streamlit_app.py` - User Interface
This script creates a simple web interface using Streamlit:
- Provides button to start the scanning process and view the results.
- Displays the outcome of the scanning and threat detection process in a user-friendly manner.

## How to Use

1. **Set Up the Environment**: Ensure all dependencies are installed as per the `Pipfile`.
2. **Run the Application**: Start the Flask app using `sudo python app.py`.(provide root priviliges for scapy to work)
3. **Start Scanning**: Use the Streamlit interface by running `streamlit run streamlit_app.py` or access it directly at [Network Scanner Streamlit App](https://networkscanner.streamlit.app).

## Requirements

- Python 3.12
- Flask
- Scrapy
- Scrapy-Selenium
- Scapy
- Streamlit

## License

This project is licensed under the MIT License.
