import requests

proxies = {
    'http':'socks5://USER:PASSWORD@SERVER',
    'https':'socks5://USER:PASSWORD@SERVER'
}

def main():
    url = 'https://ifconfig.me/ip'
    response = requests.get(url, proxies=proxies)
    print('Spoofed ip: {}'.format(response.text.strip()))


if __name__ == '__main__':
    main()
