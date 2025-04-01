# Wangsu SDK for Python

This SDK provides Python interfaces to interact with Wangsu API services.

## Installation

Install the SDK using pip:

```bash
pip install wangsu-sdk-python
```

Install the SDK for a specific product category using pip:

```bash
pip install wangsu-sdk-python-toolservice
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
from wangsu.toolservice.models import *

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
| Querybandwidthlimittasklistservice | This interface is used to query the bandwidth limit task list under the account and return detailed information of all tasks with bandwidth. The returned content includes the domain name, task name, and the set maximum bandwidth value. This interface is suitable for scenarios where traffic control policies need to be evaluated and managed, helping users quickly identify and manage the currently set bandwidth limit tasks. | POST | /api/tools/queryBandwidthLimitTaskList |
| Icpqueryservice | Query whether specified domain has been registered in MIIT of Mainland China.<br><br>Limit: call frequency of the interface cannot exceed 50 times/day. | GET | /api/icp |
| Akamaiipforbiddenservice | This interface is used to block specific IP addresses from accessing AKAMAI services. Users can do this by entering a list of IP addresses to be blocked. This interface helps users block access from untrusted or harmful IP addresses and improve network security. | POST | /api/tools/ip-forbid/akamai |
| Reportserveripcountrycodeservice | Query the CDN service IP list for specific domains in different countries. Users provide the domain and country to get the IP list of coverage nodes for that domain. It's useful for viewing global CDN service IP distribution. | POST | /api/report/service-ip/country |
| Akamaiippermitservice | Akamaiippermitservice | POST | /api/tools/ip-permit/akamai |
| Forbidorresumevisitoripsbydomainservice | Forbid and Resume guest IP addresses from accessing the domain. | POST | /api/spider/ip-forbid |
| Queryforbiddingvisitoripsbydomainservice | Query Forbidding IPs by domain, support paging query. | POST | /api/spider/ip-forbid/query |
| Ipdomainservice | This interface is used to query the domain names that are using the IP address. The user enters the IP address to obtain the list of domain names associated with the IP. The information returned by the interface includes the current usage status of the IP and the list of domain names that use the IP. In actual applications, this interface can help users detect the domain name usage of a specific IP, which is suitable for network monitoring and management. | POST | /api/tools/ip/domain-list |
| Queryallbandwidthlimittasklistservice | This interface is used to query all bandwidth restriction tasks configured under the user account. When calling, the user can choose whether to include all customer domain names involved in the task and decide whether to return information on all task status. The returned data displays detailed information on each bandwidth restriction task in a list format, including task name, category, status, and related control policies and parameters. This interface helps users manage bandwidth settings and can effectively control and process specific traffic and requests in a timely manner. | POST | /api/tools/queryAllBandwidthLimitTaskList |
| Queryforbiddingvisitoripsbylabelcodeservice | Query the forbidding IPs by LabelCode, and support pagination.<br><br> | POST | /api/spider/label-ip-forbid/query |
| Forbidorresumevisitoripsbylabelcodeservice | A customer can create a label that can be associated with multiple domains and used to forbid or resume visitor IPs through that label . This has the same effect as forbidding or resuming the designated visitor IPs for all domains associated with the label. | POST | /api/spider/label-ip-forbid/operate |
| Addorremoveforbiddingipwhitelistservice | Provide the ability to add or remove IP whitelist. Depending on its granularity, IPs in the whitelist will be filtered for "Label Granularity" and "Domain Granularity" forbidding requests.<br>Supports distributing IP whitelist at three granularities. They are as follows:<br>"Customer Granularity": IP whitelists managed at customer affect all effective domains and effective labels under that customer.It will be filtered for both "Label Granularity" and "Domain Granularity" forbidding requests.<br>"Domain Granularity": IP whitelists managed at domain affect that effective domains.It will be filtered for only 'Domain Granularity' forbidding requests.<br>"Label Granularity": IP whitelists managed at label affect that effective labels.It will be filtered for only 'Label  Granularity' forbidding requests.<br>When adding, simultaneously resume IPs that are still forbidding at the corresponding granularity. | POST | /api/spider/ip-whitelist/operate |
| Queryforbiddingipwhitelistservice | Provide the ability to query the list of IPs on the forbidding whitelist. | POST | /api/spider/ip-whitelist/query |