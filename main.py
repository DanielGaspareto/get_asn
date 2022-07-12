"""This code get asn information from bgp view API."""
import requests
from pprint import pprint


def get_asn(asn_number: int):
    """
    This method get asn information.

    :param asn_number:
    :return: json
    """
    info = requests.get(f'https://api.bgpview.io/asn/{asn_number}')

    info = info.json()

    return info


def run():
    """
    Start code.

    :return:
    """
    asn_number = int(input("Write asn number here: "))
    info = get_asn(asn_number=asn_number)
    pprint(info)
