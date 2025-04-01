# Wangsu SDK for Python

This SDK provides Python interfaces to interact with Wangsu API services.

## Installation

Install the SDK using pip:

```bash
pip install wangsu-sdk-python
```

Install the SDK for a specific product category using pip:

```bash
pip install wangsu-sdk-python-secretmanagement
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
from wangsu.secretmanagement.models import *

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
| CreateASecret | CreateASecret to protect sensitive text from being exposed in a property's Edge Logic. Refer to the secret in your property's Edge Logic using the $SECRET(secretName) syntax. When you deploy the property, references to $SECRET(secretName) will be replaced by the text. | POST | /cdn/secrets |
| GetAListOfSecrets | GetAListOfSecrets that have been defined. Filter the results using the query parameters. | GET | /cdn/secrets |
| GetASecret | Get details about a secret including its usage in properties deployed to staging and production. | GET | /cdn/secrets/* |
| UpdateASecret | UpdateASecret using this API. Deployed properties using the secret will continue to use its original value at the time of deployment. If you change the secret's name, property versions referring to the old name will not pass future validations until you edit the properties to remove the references or update them to use a valid secret's name. If you change the secret's value, properties using the secret must be revalidated before they can be redeployed.  | PATCH | /cdn/secrets/* |
| DeleteASecret | DeleteASecret by its ID. A secret used in a deployed property cannot be deleted. If a secret is obsolete, you must remove its references in properties, revalidate, and redeploy before you can delete the secret. | DELETE | /cdn/secrets/* |