import os
import subprocess

def install_module(module_name):
    subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])

try:
    import requests
except ImportError:
    print("Module 'requests' is not installed.")
    install = input("Do you want to install 'requests'? (y/n): ").strip().lower()
    if install == 'y':
        install_module('requests')
    else:
        raise ImportError("Module 'requests' is required to run this program.")

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("Module 'beautifulsoup4' is not installed.")
    install = input("Do you want to install 'beautifulsoup4'? (y/n): ").strip().lower()
    if install == 'y':
        install_module('beautifulsoup4')
    else:
        raise ImportError("Module 'beautifulsoup4' is required to run this program.")

try:
    import re
except ImportError:
    print("Module 're' is not installed.")
    install = input("Do you want to install 're'? (y/n): ").strip().lower()
    if install == 'y':
        install_module('re')
    else:
        raise ImportError("Module 're' is required to run this program.")

try:
    from termcolor import colored
except ImportError:
    print("Module 'termcolor' is not installed.")
    install = input("Do you want to install 'termcolor'? (y/n): ").strip().lower()
    if install == 'y':
        install_module('termcolor')
    else:
        raise ImportError("Module 'termcolor' is required to run this program.")

import time

def google_search(query, user_agent=None):
    url = f"https://www.google.com/search?q={query}"
    headers = {
        "User-Agent": user_agent if user_agent else "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)
    return response.text

def extract_information(html):
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    emails = list(set(re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)))
    phones = list(set(re.findall(r'\b\d{10,15}\b', text)))
    addresses = list(set(re.findall(r'\b\d{1,5}\s\w+\s\w+\b', text)))
    linkedin_links = list(set(re.findall(r'https://[a-z]{2,3}\.linkedin\.com/in/[A-Za-z0-9-]+', text)))
    facebook_links = list(set(re.findall(r'https://www\.facebook\.com/[A-Za-z0-9.]+', text)))
    twitter_links = list(set(re.findall(r'https://twitter\.com/[A-Za-z0-9_]+', text)))
    websites = list(set(re.findall(r'https?://[^\s<>"]+|www\.[^\s<>"]+', text)))
    full_names = list(set(re.findall(r'\b[A-Z][a-z]*\s[A-Z][a-z]*\b', text)))
    articles = list(set(re.findall(r'https?://[^\s<>"]+|www\.[^\s<>"]+', text)))
    return emails, phones, addresses, linkedin_links, facebook_links, twitter_links, websites, full_names, articles

def save_to_file(name, emails, phones, addresses, linkedin_links, facebook_links, twitter_links, websites, full_names, articles):
    with open(f"{name}.txt", "w") as file:
        file.write(f"Results for {name}:\n\n")
        file.write("\nFull Names:\n")
        for full_name in full_names:
            file.write(f"{full_name}\n")
        file.write("Emails:\n")
        for email in emails:
            file.write(f"{email}\n")
        file.write("\nPhones:\n")
        for phone in phones:
            file.write(f"{phone}\n")
        file.write("\nLinkedIn Links:\n")
        for link in linkedin_links:
            file.write(f"{link}\n")
        file.write("\nFacebook Links:\n")
        for link in facebook_links:
            file.write(f"{link}\n")
        file.write("\nTwitter Links:\n")
        for link in twitter_links:
            file.write(f"{link}\n")
        file.write("\nAddresses:\n")
        for address in addresses:
            file.write(f"{address}\n")
        file.write("\nWebsites:\n")
        for website in websites:
            file.write(f"{website}\n")
        file.write("\nArticles:\n")
        for article in articles:
            file.write(f"{article}\n")

def osint_dorking(query, user_agent=None):
    html = google_search(query, user_agent)
    emails, phones, addresses, linkedin_links, facebook_links, twitter_links, websites, full_names, articles = extract_information(html)
    save_to_file(query, emails, phones, addresses, linkedin_links, facebook_links, twitter_links, websites, full_names, articles)
    
    print(colored(f"\n{'='*10} Results for {query} {'='*10}\n", 'cyan', attrs=['bold']))
    print(colored("Full Names/About Their:", 'green', attrs=['bold', 'underline']))
    for full_name in full_names:
        print(colored(f"  - {full_name}", 'yellow'))
    print(colored("Emails:", 'green', attrs=['bold', 'underline']))
    for email in emails:
        print(colored(f"  - {email}", 'yellow'))
    print(colored("\nPhones:", 'green', attrs=['bold', 'underline']))
    for phone in phones:
        print(colored(f"  - {phone}", 'yellow'))
    print(colored("\nAddresses:", 'green', attrs=['bold', 'underline']))
    for address in addresses:
        print(colored(f"  - {address}", 'yellow'))
    print(colored("\nLinkedIn Links:", 'green', attrs=['bold', 'underline']))
    for link in linkedin_links:
        print(colored(f"  - {link}", 'yellow'))
    print(colored("\nFacebook Links:", 'green', attrs=['bold', 'underline']))
    for link in facebook_links:
        print(colored(f"  - {link}", 'yellow'))
    print(colored("\nTwitter Links:", 'green', attrs=['bold', 'underline']))
    for link in twitter_links:
        print(colored(f"  - {link}", 'yellow'))
    print(colored("\nWebsites:", 'green', attrs=['bold', 'underline']))
    for website in websites:
        print(colored(f"  - {website}", 'yellow'))
    print(colored("\nArticles:", 'green', attrs=['bold', 'underline']))
    for article in articles:
        print(colored(f"  - {article}", 'yellow'))
    print(colored(f"\n{'='*10} End of Results {'='*10}\n", 'cyan', attrs=['bold']))

if __name__ == "__main__":
    try:
        os.system('clear')
        print(colored(" ██████╗  ██████╗  ██████╗  ██████╗ ██╗     ███████╗ ██████╗ ███████╗██╗███╗   ██╗████████╗", 'green'))
        print(colored("██╔════╝ ██╔═══██╗██╔═══██╗██╔════╝ ██║     ██╔════╝██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝", 'green'))
        print(colored("██║  ███╗██║   ██║██║   ██║██║  ███╗██║     █████╗  ██║   ██║███████╗██║██╔██╗ ██║   ██║", 'green')) 
        print(colored("██║   ██║██║   ██║██║   ██║██║   ██║██║     ██╔══╝  ██║   ██║╚════██║██║██║╚██╗██║   ██║", 'green'))
        print(colored("╚██████╔╝╚██████╔╝╚██████╔╝╚██████╔╝███████╗███████╗╚██████╔╝███████║██║██║ ╚████║   ██║", 'green')) 
        print(colored(" ╚═════╝  ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚══════╝ ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝ V1", 'green')) 
        print("Author @505Snoop / Under Copyright @505Lab / t.me/Lab505")         
        print(" ")                                       
        print(" ") 
        print("Enter Information of Target | Ex : Ronaldo")                             
        query = input(colored("Enter information: ", 'green', attrs=['bold'])).strip()
        if query == "":
            raise ValueError("Input cannot be empty.")
        
        user_agent = input(colored("Enter custom User-Agent (leave blank to use default): ", 'green', attrs=['bold']))
        
        print(colored("Inspector finding their information 🚀", 'magenta', attrs=['bold']))
        time.sleep(0.5)
        
        osint_dorking(query, user_agent if user_agent.strip() != "" else None)
    except Exception as e:
        print(colored(f"An error occurred: {e}", 'red', attrs=['bold']))
