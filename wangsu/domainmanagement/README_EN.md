# Wangsu SDK for Python

This SDK provides Python interfaces to interact with Wangsu API services.

## Installation

Install the SDK using pip:

```bash
pip install wangsu-sdk-python
```

Install the SDK for a specific product category using pip:

```bash
pip install wangsu-sdk-python-domainmanagement
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
from wangsu.domainmanagement.models import *

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
| Cancelapidomainservice | Cancel the CDN acceleration service of the specified domain, that is, force the request to back to source directly from the DNS level. It is mostly used for customers not responding in time to deal with Yellow-Related websites, and so on. | PUT | /api/domain/*/cancel |
| Restoreapidomainservice | Restore the CDN acceleration service of the specified domain, that is, let the request return to the CDN node. | PUT | /api/domain/*/restore |
| Enablesingledomainservice | Enable an accelerated domain with a state of "disabled" and provide accelerated service with an existing configuration. | PUT | /api/domain/*/enable |
| Disablesingledomainservice | Disables the specified accelerated domain name, and requests for the accelerated domain name after it is disabled will be rejected directly and will not be back to origin. | PUT | /api/domain/*/disable |
| Deleteapidomainservice | Delete one of the added accelerator domains. Cannot be enabled after deletion, only the accelerated domain name can be re-created. | DELETE | /api/domain/* |
| Getfuzzypagingdomainlist | Queries all, or specified, acceleration domains and states under the user's account. Each acceleration domain name contains profile information. The returned accelerated domain name list is sorted in alphabetical order of the initials. | POST | /api/domain/domainList |
| Querydomainbyoriginip | Query the list of all domain name names corresponding to the source station IP under the user account. | GET | /api/originaldomainlist |
| Createdomain | Create a domain. | POST | /api/domain |
| Queryapidomainlistservice | Query all the accelerated domain names and states indicated by the user account or the specific cname-label. Each accelerated domain name contains summary information, and the returned accelerated domain name list is sorted in alphabetical order.<br>Note: Offline domains("enabled" value equals false) could not be modified. | GET | /api/domain |
| Querycustomerdomainnamegroupservice | This interface is used to query the domain information under the customer's domain group. Users can use this interface to retrieve one or more domain groups. The interface returns the basic information of each domain group and the list of domain names it contains. This interface is suitable for scenarios where multiple domain groups need to be managed, and helps users obtain the corresponding business domain name set according to different business scenarios. | POST | /api/report/domainlist/domain |
| Queryapidomainattribution | Get domain list. | GET | /api/domainlist |
| Controldomain | Used to query user's domain name and domain name information. | POST | /clouddns/Controldomain |
| Deldispatchdomain | Used to batch delete domains. Takes one minute to take effect. | POST | /clouddns/Deldispatchdomain |
| Adddomain | Used to add domains. CloudDNS supports batch add domains. Take effect in seconds. | POST | /clouddns/Adddomain |
| Deletedomain | Used to batch delete domains. Take effect in seconds. | POST | /clouddns/DelDomain |
| Adddispatchdomain | Used to add dispatch domain. Takes one minute to take effect. | POST | /clouddns/Adddispatchdomain |
| Querydispatchdomains | Used to query the dispatch domain and domain details of users. | POST | /clouddns/Querydispatchdomains |
| Querydomains | Used to query domains and domain details of users. | POST | /clouddns/Querydomains |
| Dispatchwarnlog | Querying the Scheduling Alarm Log | POST | /clouddns/Dispatchwarnlog |
| Updatedispatchdomain | Edit Scheduling Domain Name | POST | /clouddns/Updatedispatchdomain |
| Controldispatchdomain | Start or stop scheduling domain name | POST | /clouddns/Controldispatchdomain |
| Channelaccetype | Query the channels and their acceleration types for the customer. | POST | /myview/Channelaccetype |
| Adddomaingroup | Domain group can group domain, making it easy for you to quickly query data by domain group.<br>This API provides create domain group functionality | POST | /api/report/domainlist/domaingroup/add |
| Editdomaingroup | Domain group can group domain, making it easy for you to quickly query data by domain group.<br>This API provides edit domain group functionality | POST | /api/report/domainlist/domaingroup/edit |
| Getpagingdomainlist | Queries all, or specified, acceleration domains and states under the user's account. Each acceleration domain name contains profile information. The returned accelerated domain name list is sorted by version. | POST | /api/domain/list |
| Querycustomeranycastipforwplus | QueryCustomerAnycastIP | GET | /api/anycast-ips |
| Predeploychangeserverconfig | Predeployed change server. The interface * can be domain name or domain id. | PUT | /api/predeploy/changeserver/* |
| Updatechangeserver | Update change server. The interface * can be domain name or domain id. | PUT | /api/config/changeserver/* |
| Querychangeserver | Query change server. The interface * can be domain name or domain id. | GET | /api/config/changeserver/* |
| Enablecdndomainservice | Enable an accelerated domain with a state of "disabled" and provide accelerated service with an existing configuration. | PUT | /cdn/domains/*/enable |
| Disablecdndomainservice | Disables the specified accelerated domain name, and requests for the accelerated domain name after it is disabled will be rejected directly and will not be back to origin. | PUT | /cdn/domains/*/disable |
| Deletecdndomainservice | Delete one of the added accelerator domains. Cannot be enabled after deletion, only the accelerated domain name can be re-created. | DELETE | /cdn/domains/* |
| Updatecustomeranycastiprecordstatus | Update the record status of Anycast IP | POST | /api/anycast-ips/record-status |
| Deletehwdomain | Delete a HW accelerated domain that has been added. By specifying the domain name in the URI, the HW accelerated domain can be deleted. After deletion, the domain will stop accelerating. For example: /v1/domain/www.test.com. | DELETE | /v1/domain/* |
| Enabledisablehwdomain | Enable or Disable Hw Domain.For example: If "state" is set to "online", it means the domain is enabled. If "state" is set to "offline", it means the domain is disabled. | PUT | /v1/domain/*/state |