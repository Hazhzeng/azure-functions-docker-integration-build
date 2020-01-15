import argparse
import requests

LIST_ENDPOINT = 'ListServiceFabricImages'
REMOVE_ENDPOINT = 'RemoveServiceFabricImage'
REMOVE_CONFIG_ENDPOINT = 'RemoveServiceFabricImageConfiguration'


def parse_args():
    parser = argparse.ArgumentParser(
        description='Remove Mesh Image')
    parser.add_argument('--proxy-address', dest='proxy_address')
    parser.add_argument('--proxy-username', dest='proxy_username')
    parser.add_argument('--proxy-password', dest='proxy_password')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    list_address = '/'.join([args.proxy_address, LIST_ENDPOINT])
    list_response = requests.get(url=list_address,
                                 auth=(args.proxy_username, args.proxy_password))
    image_list = list_response.json()['value']['listOfImages']

    remove_address = '/'.join([args.proxy_address, REMOVE_ENDPOINT])
    remove_config_address = '/'.join([args.proxy_address, REMOVE_CONFIG_ENDPOINT])
    for image_name in image_list:
        delete_data = {
            'image': image_name
        }
        requests.delete(url=remove_address, json=delete_data,
                        auth=(args.proxy_username, args.proxy_password))
        requests.delete(url=remove_config_address, json=delete_data,
                        auth=(args.proxy_username, args.proxy_password))
