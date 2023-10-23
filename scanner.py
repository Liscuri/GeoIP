from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
import requests
import json

api_access_key = '42f4e5255c4b38ef3e775c9ebfc77c0a'


def main():
    print(f"""{Fore.RED}                                                             
          _____         ______           _____           ____      _____   
      ___|\    \    ___|\     \     ____|\    \         |    | ___|\    \  
     /    /\    \  |     \     \   /     /\    \        |    ||    |\    \ 
    |    |  |____| |     ,_____/| /     /  \    \       |    ||    | |    |
    |    |    ____ |     \--'\_|/|     |    |    |      |    ||    |/____/|
    |    |   |    ||     /___/|  |     |    |    |      |    ||    ||    ||
    |    |   |_,  ||     \____|\ |\     \  /    /|      |    ||    ||____|/
    |\ ___\___/  /||____ '     /|| \_____\/____/ |      |____||____|       
    | |   /____ / ||    /_____/ | \ |    ||    | /      |    ||    |       
     \|___|    | / |____|     | /  \|____||____|/       |____||____|       
       \( |____|/    \( |_____|/      \(    )/            \(    \(         
        '   )/        '    )/          '    '              '     '         
            '              '                                               
        """)

    ip = input(f"{Fore.RED}Input the IP you want to lookup!\n")
    url = f"http://api.ipstack.com/{ip}?access_key={api_access_key}"
    response = requests.get(url)
    try:
        data = json.loads(response.text)
        if 'error' in data:
            print(f"{Fore.RED}Error: {data['error']['info']}")
            main()
        else:
            print(f"""
{Fore.BLUE}ip: {data['ip']}
{Fore.BLUE}Type: {data['type']}
{Fore.BLUE}Continent Name: {data['continent_name']}
{Fore.BLUE}Country Name: {data['country_name']}
{Fore.BLUE}Region Name: {data['region_name']}
{Fore.BLUE}City: {data['city']}
{Fore.BLUE}Zip: {data['zip']}
{Fore.BLUE}Latitude: {data['latitude']}
{Fore.BLUE}Longitude: {data['longitude']}
{Fore.BLUE}Calling Code: {data['location']['calling_code']}
""")
    except json.JSONDecodeError as e:
        print(f"{Fore.RED}Error decoding the API response: {str(e)}")
    except requests.RequestException as e:
        print(f"{Fore.RED}Error making the API request: {str(e)}")


if __name__ == '__main__':
    main()
