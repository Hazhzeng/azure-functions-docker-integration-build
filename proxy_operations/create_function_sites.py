import argparse
import requests

CREATE_ENDPOINT = 'CreateFunctionSite'

V2_LANGUAGES = {
    'python': ['36', '37'],
    'node': ['8', '10'],
    'dotnet': ['2']
}

V2_LINUXFX_VERSION = {
    'python': {
        '36': 'PYTHON|3.6',
        '37': 'PYTHON|3.7'
    },
    'node': {
        '8': 'NODE|8.0',
        '10': 'NODE|10.2'
    }
}

RUNTIMES_TEST_MATRIX = {
    'v2': V2_LANGUAGES
}


def parse_args():
    parser = argparse.ArgumentParser(
        description='Create Subscription')
    parser.add_argument('--proxy-address', dest='proxy_address')
    parser.add_argument('--proxy-username', dest='proxy_username')
    parser.add_argument('--proxy-password', dest='proxy_password')
    parser.add_argument('--subscription', dest='subscription')
    parser.add_argument('--webspace', dest='webspace')
    parser.add_argument('--storage-account', dest='storage_account')
    return parser.parse_args()


def append_v2_linuxfx_version(create_data, language, version):
    # Apply linuxFxVersion to
    if V2_LINUXFX_VERSION.get(language, {}).get(version):
        create_data['linuxFxVersion'] = V2_LINUXFX_VERSION[language][version]


if __name__ == '__main__':
    args = parse_args()

    create_address = '/'.join([args.proxy_address, CREATE_ENDPOINT])

    for runtime, languages in RUNTIMES_TEST_MATRIX.items():
        for language, versions in languages.items():
            for version in versions:
                app_name = f'{runtime}-{language}-{version}'

                app_settings = {
                    'AZURE_FUNCTIONS_ENVIRONMENT': 'development',
                    'FUNCTIONS_WORKER_RUNTIME': f'{language}',
                    'FUNCTIONS_EXTENSION_VERSION': '~2',
                    'AzureWebJobsStorage': f'{args.storage_account}'
                }

                app_settings_joined = ','.join([f'{setting}={value}'
                                                for setting, value
                                                in app_settings.items()])

                create_data = {
                    'subscriptionName': args.subscription,
                    'webSpaceName': args.webspace,
                    'name': app_name,
                    'isLinux': True,
                    'appSettings': app_settings_joined
                }
                append_v2_linuxfx_version(create_data, language, version)

                create_response = requests.post(url=create_address,
                                                json=create_data,
                                                auth=(args.proxy_username,
                                                      args.proxy_password))

                print(f'Status Code for site {app_name}: ',
                      create_response.status_code)

                print(create_response.text)
