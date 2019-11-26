import argparse
import requests
import time

UPDATE_ENDPOINT = 'AddOrUpdateServiceFabricImageConfiguration'
ADD_ENDPOINT = 'AddServiceFabricImage'


def parse_args():
    parser = argparse.ArgumentParser(
        description='Mesh Image Update')
    parser.add_argument('--image-name', dest='image_name')
    parser.add_argument('--proxy-address', dest='proxy_address')
    parser.add_argument('--proxy_username', dest='proxy_username')
    parser.add_argument('--proxy_password', dest='proxy_password')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    update_data = {
        'image': args.image_name,
        'hostNameType': 'Standard',
        'numberMinimumContainers': 3,
        'maxContainersLimit': 9,
        'cpuLimit': 1.0,
        'memoryLimit': 1.75,
        'bufferRatio': 0.2,
        'placeholderId': 'v=1,k=f,e=~2,a=0',
        'tagSpecific': False
    }

    update_address = '/'.join([args.proxy_address, UPDATE_ENDPOINT])
    update_response = requests.post(url=update_address, json=update_data,
                                    auth=(args.proxy_username, args.proxy_password))

    # Sleep to allow changes to propagate
    time.sleep(10)

    add_data = {
        'image': args.image_name
    }

    add_address = '/'.join([args.proxy_address, ADD_ENDPOINT])
    requests.post(url=add_address, json=add_data,
                  auth=(args.proxy_username, args.proxy_password))
