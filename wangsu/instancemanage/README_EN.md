# Wangsu SDK for Python

This SDK provides Python interfaces to interact with Wangsu API services.

## Installation

Install the SDK using pip:

```bash
pip install wangsu-sdk-python
```

Install the SDK for a specific product category using pip:

```bash
pip install wangsu-sdk-python-instancemanage
```


## Requirements

- Python 3.6 or later
- Dependencies:
  - requests >= 2.10.0
  - alibabacloud_tea >= 0.3.3
  - alibabacloud_tea_openapi >= 0.3.6
  - alibabacloud_tea_console >= 0.0.1
  - alibabacloud_tea_util >= 0.3.8

## Quick Start

### Example

The SDK uses AKSK authentication. You need to configure your access key and secret key:

```python
import json
from wangsu.common.auth.AkSkConfig import AkSkConfig
from wangsu.common.auth.AkSkAuth import AkSkAuth
from wangsu.instancemanage.models import *

# Refer to the API list at the end of this document and modify the corresponding {ActionName}, Method, Uri
request = {ActionName}Request()

aksk_config = AkSkConfig()
aksk_config.access_key = "YOUR_ACCESS_KEY"
aksk_config.secret_key = "YOUR_SECRET_KEY"
aksk_config.uri = "/your/api/path"
aksk_config.method = "GET"  # HTTP method: GET, POST, PUT, DELETE, etc.

# Convert request to JSON and make the API call
response = AkSkAuth.invoke(aksk_config, json.dumps(request.to_map()))
print(response)

```



## API List
For detailed API documentation and available methods, please refer to the [official Wangsu API documentation](https://www.wangsu.com/document/api-doc/Overview?productType=all).

| ActionName | enDescription | client_methods | uri |
| --- | --- | --- | --- |
| Vmpremoveinstance | Destroy the specified instance, supporting batch destruction. After destruction, all physical resources used by the instance will be reclaimed, including disks and snapshots. All related data will be lost and permanently irreparable. | POST | /vmp/servers/delete |
| Vmpqueryinstance | instance query | GET | /vmp/servers |
| Vmpinstanceoperation | If you find that an instance is not functioning properly (such as being able to ping but unable to log in), you can call the interface to attempt to forcibly restart the machine. Forcing a reboot is equivalent to a traditional server power outage reboot, which may result in the loss of data in the instance operating system that has not been written to the disk. A normal shutdown is a normal shutdown operation. After successfully calling the interface, it is necessary to call the instance query interface again to confirm the latest status of the instance and verify whether the restart was successful. | POST | /vmp/servers/*/action |
| Vmpcreateinstance | Through this interface, you can apply for a cloud host instance of a specified specification in a certain region. After the instance is created, you can obtain the latest status of the instance by using the instance query interface. | POST | /vmp/servers |
| Editinstance | Used to modify instance information. Currently, only instance name modification is supported. | PUT | /vmp/servers |
| Instanceipv6management | Assign/remove IPv6 addresses for existing cloud host instances, and bare metal instances do not support it.<br>Instructions for assigning IPv6:<br>1) Action=ALLOCATION;<br>2) The instance status must be running or down, and the node where the host is located must support IPv6;<br>3) If the instance already has IPv6, the interface will directly return the existing IPv6 address.<br>Instructions for removing IPv6:<br>1) Action=REMOVE;<br>2) The instance state must be running or down. | POST | /vmp/servers/ipv6 |
| Instancediskscaling | Supports attaching disks to instances online. | POST | /vmp/servers/attachDisk |
| Manageinstancetags | Manage virtual machine instance labels and support modifying or deleting instance labels. | PUT | /vmp/server-tags |
| Convertfreetypeinstancetochargetype | Convert free type instance to charge type.Transfer the designated free instances to regular status to prevent them from being deleted upon expiration, and support batch transfer to regular status. After being confirmed, the instance will be converted to a billing instance. | POST | /vmp/servers/charge |
| Instancereplaceip | Replace virtual machine IP, this function supports simultaneous replacement of multiple IPs, but note that each virtual machine can only be replaced once | PUT | /vmp/servers/ipReplace |
| InstanceRebuild | Through this api, it is possible to reinstall the system for the already created instances. | POST | /vmp/servers/rebuild |
| Createdeployment | create a ecci deployment | POST | /api/ecci/v1/deployments |
| Getecciinstance | get ecci instance detail | GET | /api/ecci/v1/instances/* |
| Updateecciinstance | update a ecci instance | PUT | /api/ecci/v1/instances/* |
| Deleteecciinstance | delete a ecci instance | DELETE | /api/ecci/v1/instances/* |
| Getecciinstancelist | get ecci instances list | GET | /api/ecci/v1/instances |
| Getclusterlist | get clusters list | GET | /api/ecci/v1/clusters |
| Gettoken | get auth token | GET | /api/ecci/v1/token |
| Createephoneinstance | Create ephone instance | POST | /ephone/instances/create |
| Manageephoneinstance | Operate the specified edge cloud phone instance, including edge cloud phone delete, reboot, and one-click new operations. Note that a reboot may lose data in the edge cloud phone instance that is not written to disk, or a one-click new machine may lose all disk data in the cloud edge phone instance. | POST | /ephone/instances/action |
| Queryinstancelist | Queries the specified edge cloud ephone instance interface. | GET | /ephone/instances/list |
| Instancebandwidthaggregationquery | Virtual Machine Bandwidth Summary Query Interface, where users query the total traffic of virtual machines within a certain period of time, in MB. extTrafficIn: the total inbound traffic of the external network, extTrafficOut: the total outbound traffic of the external network. | GET | /vmp/servers/bandwidth_aggregation |
| Querygps | Querying the GPS coordinates of an ephone instance. | GET | /ephone/instances/gps |
| Runephoneadbshell | This interface allows you to execute adb shell commands in the ephone instance | POST | /ephone/instances/adbshell |
| Screenshotephoneinstance | Take a screenshot of the specified cloud phone instance. | POST | /ephone/instances/screenshot |
| Vmpinstancebandwidth5minquery | Query instance single-node 5-minute granularity bandwidth data.<br> | GET | /vmp/servers/bandwidth_5_minutes |