## Overview

This python script gets the metadata of an EC2 instance. Please note that this script should only be executed from within the EC2 instance you want to get its metadata. i.e after you have SSH'ed into the instance.

### Requirements
- `python3` required

### Usage

- To get the all the metadata of an EC2 instance in json:

    ```python3 get_ec2_metadata.py```

    Response:
    ```
        {
            'accountId': 'xxxxxx',
            'architecture': 'x86_64',
            'availabilityZone': 'us-east-1e',
            'billingProducts': None,
            'devpayProductCodes': None,
            'marketplaceProductCodes': None,
            'imageId': 'ami-09d95fab7fff3776c',
            'instanceId': 'i-xxxxx',
            'instanceType': 't2.micro',
            'kernelId': None,
            'pendingTime': '2021-10-20T20:48:33Z',
            'privateIp': 'xxx.xx.xx.xxx',
            'ramdiskId': None,
            'region': 'us-east-1',
            'version': '2017-09-30'
        }
    ```

- To get the value for any metadata key of an EC2 instance, in the example below for accountId:

    ```python3 get_ec2_metadata.py --ec2_metadata_key accountId```

    Response:

    ```EC2 metadata value for accountId:  xxxxxxxxxx```