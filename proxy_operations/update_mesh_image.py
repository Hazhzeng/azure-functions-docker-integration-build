import argparse
import requests
import time

UPDATE_CONFIG_ENDPOINT = 'AddOrUpdateServiceFabricImageConfiguration'
ADD_ENDPOINT = 'AddServiceFabricImage'


def parse_args():
    parser = argparse.ArgumentParser(description='Mesh Image Update')
    parser.add_argument('--image-name', dest='image_name')
    parser.add_argument('--proxy-address', dest='proxy_address')
    parser.add_argument('--proxy-username', dest='proxy_username')
    parser.add_argument('--proxy-password', dest='proxy_password')
    parser.add_argument('--placeholder-id', dest='placeholder_id')
    parser.add_argument('--hostname-type', dest='hostname_type')
    parser.add_argument('--min-containers', dest='min_containers', default=3, type=int)
    parser.add_argument('--max-containers', dest='max_containers', default=5, type=int)
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    update_data = {
        'image': args.image_name,
        'hostNameType': args.hostname_type,
        'numberMinimumContainers': args.min_containers,
        'maxContainersLimit': args.max_containers,
        'cpuLimit': 1.0,
        'memoryLimit': 1.75,
        'bufferRatio': 0.2,
        'placeholderId': args.placeholder_id,
        'tagSpecific': False
    }

    update_address = '/'.join([args.proxy_address, UPDATE_CONFIG_ENDPOINT])
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
