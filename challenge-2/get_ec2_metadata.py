#!/usr/bin/python3
'''
This python script gets the metadata of an EC2 instance. 
If a key is provided, the corresponding value is retrieved, provided the key exists in the EC2 metadata object.
Please note that this script should only be executed from within the EC2 instance you want to get its metadata. i.e after you have SSH'ed onto the instance.

Usage:
- To get the all the metadata of an EC2 instance in json:
    python3 get_ec2_metadata.py

- To get the value for any metadata key of an EC2 instance:

    python3 get_ec2_metadata.py --ec2_metadata_key accountId
'''

import json
import urllib.request
import argparse


class NonExistentEC2MetadatKey(Exception):
    '''
    Raised when the give metdata key does not exist in the EC2 metadata object
    '''
    pass


def get_ec2_metadata(ec2_metadata_key=None):
    metadata = urllib.request.urlopen(
        "http://169.254.169.254/latest/dynamic/instance-identity/document"
    ).read()

    formatted_metadata = json.loads(metadata)

    if ec2_metadata_key:
        if ec2_metadata_key not in formatted_metadata.keys():
            raise NonExistentEC2MetadatKey('Non existent EC2 metadata key provided')

        return formatted_metadata[ec2_metadata_key]

    return formatted_metadata


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--ec2_metadata_key",
        type=str,
        help="EC2 metadata key value to retrieve"
    )
    args = parser.parse_args()
    ec2_metadata_key = args.ec2_metadata_key

    if ec2_metadata_key:
        print(f'EC2 metadata value for {ec2_metadata_key}: ',
              get_ec2_metadata(ec2_metadata_key))
    else:
        print(json.dumps(get_ec2_metadata(), indent=4))
