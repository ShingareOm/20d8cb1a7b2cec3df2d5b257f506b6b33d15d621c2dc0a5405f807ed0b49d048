#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Pimp Dorker
Author: Om Shingare
GitHub: https://github.com/ShingareOm
"""

import sys
import time
import os
from urllib.parse import urlparse
from googlesearch import search

class Colors:
    RED = "\033[91m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    RESET = "\033[0m"

def display_banner():
    banner = f"""
{Colors.RED}
            d8,                              d8b                   d8b       
           `8P                               88P                   ?88       
                                            d88                     88b      
?88,.d88b,  88b  88bd8b,d88b ?88,.d88b, d888888   d8888b   88bd88b  888  d88'
`?88'  ?88  88P  88P'`?8P'?8b`?88'  ?88d8P' ?88  d8P' ?88  88P'  `  888bd8P' 
  88b  d8P d88  d88  d88  88P  88b  d8P88b  ,88b 88b  d88 d88      d88888b   
  888888P'd88' d88' d88'  88b  888888P'`?88P'`88b`?8888P'd88'     d88' `?88b,
  88P'                         88P'                                          
 d88                          d88                                     V 1.0  
 ?8P                          ?8P                                            
{Colors.RESET}
"""
    print(banner)
    print(f"{Colors.BLUE}Author: Om Shingare | Pimp Dorker")
    print("GitHub: https://github.com/ShingareOm")
    print(f"{Colors.RESET}")

def create_folder(folder_name):
    try:
        os.makedirs(folder_name, exist_ok=True)
        print(f"{Colors.GREEN}[+] Folder created: {folder_name}{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}[!] Error creating folder: {e}{Colors.RESET}")
        sys.exit(1)

def save_to_file(filepath, data):
    try:
        with open(filepath, "a", encoding="utf-8") as file:
            file.write(data + "\n")
    except Exception as e:
        print(f"{Colors.RED}[!] Error saving to file: {e}{Colors.RESET}")

def extract_main_domain(url):
    try:
        domain = urlparse(url).netloc
        if domain.startswith("www."):
            domain = domain[4:]
        return domain
    except Exception:
        return None

def perform_dork_search(query, amount, folder_name):
    all_links_file = os.path.join(folder_name, "all_links.txt")
    main_domains_file = os.path.join(folder_name, "main_domains.txt")

    print(f"\n{Colors.BLUE}[~] Searching for: {query}{Colors.RESET}\n")

    try:
        for index, result in enumerate(search(query, num_results=amount), start=1):
            print(f"[{index}] {result}")

            # Save full URL
            save_to_file(all_links_file, result)

            # Save main domain
            main_domain = extract_main_domain(result)
            if main_domain:
                save_to_file(main_domains_file, main_domain)

            time.sleep(0.1)

    except KeyboardInterrupt:
        print(f"\n{Colors.RED}[!] Search interrupted by user. Exiting...{Colors.RESET}")
        sys.exit(0)
    except Exception as e:
        print(f"{Colors.RED}[!] An error occurred: {e}{Colors.RESET}")

def get_user_input():
    query = input("\n[+] Enter the Dork Search Query: ").strip()
    while True:
        try:
            amount = int(input("[+] Enter the Number of Results to Display: ").strip())
            if amount > 0:
                break
            else:
                print(f"{Colors.RED}[!] Please enter a positive integer.{Colors.RESET}")
        except ValueError:
            print(f"{Colors.RED}[!] Invalid input. Please enter a number.{Colors.RESET}")

    return query, amount

def main():
    display_banner()

    # Get folder name from command-line argument or user input
    if len(sys.argv) > 1:
        folder_name = sys.argv[1]
    else:
        folder_name = input("[+] Enter the folder name to save results: ").strip()

    create_folder(folder_name)

    try:
        query, amount = get_user_input()
        perform_dork_search(query, amount, folder_name)
        print(f"{Colors.GREEN}[~] Done! Results saved in {folder_name}.{Colors.RESET}")
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}[!] Program interrupted by user. Exiting...{Colors.RESET}")

if __name__ == "__main__":
    main()
