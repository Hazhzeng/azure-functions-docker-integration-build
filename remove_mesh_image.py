import argparse
import requests

LIST_ENDPOINT = 'ListServiceFabricImages'
REMOVE_ENDPOINT = 'RemoveServiceFabricImage'


def parse_args():
    parser = argparse.ArgumentParser(
        description='Remove Mesh Image')
    parser.add_argument('--proxy-address', dest='proxy_address')
    parser.add_argument('--username', dest='username')
    parser.add_argument('--password', dest='password')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    list_address = '/'.join([args.proxy_address, LIST_ENDPOINT])
    list_response = requests.get(url=list_address,
                                 auth=(args.username, args.password))
    image_list = list_response.json()['value']['listOfImages']

    remove_address = '/'.join([args.proxy_address, REMOVE_ENDPOINT])
    for image_name in image_list:
        delete_data = {
            'image': image_name
        }
        requests.delete(url=remove_address, json=delete_data,
                        auth=(args.username, args.password))
