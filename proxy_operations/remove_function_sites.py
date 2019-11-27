import argparse
import requests

DELETE_ENDPOINT = 'DeleteWebSite'

V2_LANGUAGES = {
    'python': ['36', '37'],
    'node': ['8', '10'],
    'dotnet': ['2']
}

RUNTIMES_TEST_MATRIX = {
    'v2': V2_LANGUAGES
}

def parse_args():
    parser = argparse.ArgumentParser(
        description='Remove Function Sites')
    parser.add_argument('--proxy-address', dest='proxy_address')
    parser.add_argument('--proxy-username', dest='proxy_username')
    parser.add_argument('--proxy-password', dest='proxy_password')
    parser.add_argument('--subscription', dest='subscription')
    parser.add_argument('--webspace', dest='webspace')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    delete_address = '/'.join([args.proxy_address, DELETE_ENDPOINT])

    for runtime, languages in RUNTIMES_TEST_MATRIX.items():
        for language, versions in languages.items():
            for version in versions:
                app_name = f'{runtime}-{language}-{version}'

                delete_data = {
                    'subscriptionName': args.subscription,
                    'webSpaceName': args.webspace,
                    'name': app_name
                }

                delete_response = requests.delete(url=delete_address,
                                                json=delete_data,
                                                auth=(args.proxy_username,
                                                      args.proxy_password))

                print(f'Status Code for site {app_name}: ',
                      delete_response.status_code)

                print(delete_response.text)
