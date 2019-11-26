import argparse
import requests

CREATE_ENDPOINT = 'CreateUser'


def parse_args():
    parser = argparse.ArgumentParser(
        description='Create User')
    parser.add_argument('--proxy-address', dest='proxy_address')
    parser.add_argument('--proxy-username', dest='proxy_username')
    parser.add_argument('--proxy-password', dest='proxy_password')
    parser.add_argument('--publishing-username', dest='publishing_username')
    parser.add_argument('--publishing-password', dest='publishing_password')
    parser.add_argument('--name', dest='name')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    create_address = '/'.join([args.proxy_address, CREATE_ENDPOINT])

    create_data = {
        'name': args.name,
        'publishingUserName': args.publishing_username,
        'publishingPassword': args.publishing_password
    }

    create_response = requests.post(url=create_address,
                                    json=create_data,
                                    auth=(args.proxy_username,
                                          args.proxy_password))

    print('Status Code: ', create_response.status_code)
    print(create_response.text)
