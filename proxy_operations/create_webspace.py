import argparse
import requests

CREATE_ENDPOINT = 'CreateWebSpace'


def parse_args():
    parser = argparse.ArgumentParser(
        description='Create Webspace')
    parser.add_argument('--proxy-address', dest='proxy_address')
    parser.add_argument('--proxy-username', dest='proxy_username')
    parser.add_argument('--proxy-password', dest='proxy_password')
    parser.add_argument('--subscription', dest='subscription')
    parser.add_argument('--plan', dest='plan', default="DefaultPlan")
    parser.add_argument('--name', dest='name')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    create_address = '/'.join([args.proxy_address, CREATE_ENDPOINT])

    create_data = {
        "subscriptionName": args.subscription,
        "name": args.name,
        "plan": args.plan,
    }

    create_response = requests.post(url=create_address,
                                    json=create_data,
                                    auth=(args.proxy_username,
                                          args.proxy_password))

    print('Status Code: ', create_response.status_code)
    print(create_response.text)
