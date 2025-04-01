# Wangsu SDK for Python

This SDK provides Python interfaces to interact with Wangsu API services.

## Installation

Install the SDK using pip:

```bash
pip install wangsu-sdk-python
```

Install the SDK for a specific product category using pip:

```bash
pip install wangsu-sdk-python-sharedconfiguration
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
from wangsu.sharedconfiguration.models import *

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
| Listsharedwafruleexceptions | Return a list of WAF Rule Exceptions for the shared configuration. | POST | /api/v1/waf/share/exception/get-list |
| Createsharedwafruleexception | Create a WAF rule exception to shared configurations. | POST | /api/v1/waf/share/exception/create |
| Updatesharedwafruleexception | Modify the configuration of WAF Rule Exception in the shared configuration. | POST | /api/v1/waf/share/exception/update |
| Deletesharedwafruleexception | Delete the WAF rule exceptions in the shared configuration. | POST | /api/v1/waf/share/exception/delete |
| Createcustomaction | Create a custom action,up to 5 custom response actions can be configured. | POST | /api/v1/share-action/add-customize-act |
| Listcustomactions | Return a list of custom actions. | POST | /api/v1/share-action/get-customize-act-list |
| Updatecustomaction | Update the configuration of a custom action. | POST | /api/v1/share-action/update-customize-act |
| Deletecustomactions | Delete custom actions. Note: the referenced custom action cannot be deleted. | POST | /api/v1/share-action/delete-customize-act-batch |
| Createsharedwhitelistrule | Create a Whitelist rule for shared configurations. | POST | /api/v1/common/share-whitelist/add |
| Updatesharedwhitelistrule | Modify a Whitelist rule's configuration for the shared configuration. | POST | /api/v1/common/share-whitelist/update |
| Deletesharedwhitelistrule | Delete the Whitelist rules for the shared configuration. | POST | /api/v1/common/share-whitelist/delete |
| Listsharedwhitelistrules | Return a list of Whitelist rules for shared configurations. | POST | /api/v1/common/share-whitelist/get-list |
| Createsharedratelimitingrule | Create a Rate Limiting rule for shared configurations. | POST | /api/v1/share-rate-limit/add-rule |
| Updatesharedratelimitingrule | Modify a Rate Limiting rule's configuration for the shared configuration. | POST | /api/v1/share-rate-limit/update-rule |
| Deletesharedratelimitingrule | Delete the Rate Limiting rules for the shared configuration. | POST | /api/v1/share-rate-limit/delete-by-ids |
| Listsharedratelimitingrules | Return a list of Rate Limiting rules for shared configurations. | POST | /api/v1/share-rate-limit/get-rule-list |
| Createappapiexceptionfeature | Create APP/API exception feature. | POST | /api/v1/dms/service-feature/add |
| Queryappapiexceptionlist | Query APP/API exception list. | POST | /api/v1/dms/service-feature/get-list |
| Deleteappapiexceptionfeature | Delete APP/API exception feature. | POST | /api/v1/dms/service-feature/delete |
| Queryappapiexceptionfeaturedetail | Query APP/API exception feature details(Share Configurations). | POST | /api/v1/dms/service-feature/get-detail |
| Queryappapiexceptionfeaturereferencedhostnames | Query APP/APIException Feature Referenced Hostnames(Share Configurations). | POST | /api/v1/dms/service-feature/get-relate-domain-list |
| Updateshareconfigurationsappapiexceptionfeature | Modify App/API exceptions(ShareConfigurations). | POST | /api/v1/dms/service-feature/update |
| Listsharedcustomrules | Return a list of  custom rules for shared configurations. | POST | /api/v1/share-customize-rule/get-list |
| Disassociateshareratelimit | Disassociate shared configuration rate limit rule from Hostname. | POST | /api/v1/common/share-rate-limit/disassociate |
| Associateshareratelimit | Associate shared configuration rate limit rule from Hostname. | POST | /api/v1/common/share-rate-limit/associate |
| Associatesharecustomizerule | Associate shared configuration custom rule from Hostname. | POST | /api/v1/common/share-customize-rule/associate |
| Disassociatesharecustomizerule | Disassociate shared configuration custom rule from Hostname. | POST | /api/v1/common/share-customize-rule/disassociate |
| Associatesharecustomizebots | Associate shared configuration custom Bots from Hostname. | POST | /api/v1/common/share-customize-bots/associate |
| Disassociatesharecustomizebots | Disassociate shared configuration custom Bots from Hostname. | POST | /api/v1/common/share-customize-bots/disassociate |
| Associatesharedwhitelistrule | Associate shared configuration Whitelist rule from Hostname. | POST | /api/v1/common/share-whitelist/associate |
| Disassociatesharedwhitelistrule | Disssociate shared configuration Whitelist rule from Hostname. | POST | /api/v1/common/share-whitelist/disassociate |
| Associatedmsshareservicefeature | Associate the shared configuration APP/API exception with the domain name. | POST | /api/v1/dms/service-feature/relateDomains |
| Disassociatedmsshareservicefeature | Disassociate the shared configuration app/API exception from the domain name. | POST | /api/v1/dms/service-feature/disRelateDomains |