import requests
import argparse

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
        description='Create Subscription')
    parser.add_argument('--zipdeploy-address', dest='zipdeploy_address')
    parser.add_argument('--site-username', dest='site_username')
    parser.add_argument('--site-password', dest='site_password')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    for runtime, languages in RUNTIMES_TEST_MATRIX.items():
        for language, versions in languages.items():
            for version in versions:
                app_name = f'{runtime}-{language}-{version}'
                file_name = f'{runtime}_{language}_{version}.zip'
                fileobj = open(file_name, 'rb')
                r = requests.post(f'https://{app_name}.scm.{args.zipdeploy_address}',
                                  auth=(args.site_username, args.site_password),
                                  files={'archive': (file_name, fileobj)},
                                  verify=False)

                print(f'Deploy status code for app {app_name}: ', r.status_code)
