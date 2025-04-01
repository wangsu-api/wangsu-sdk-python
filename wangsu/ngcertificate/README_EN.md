# Wangsu SDK for Python

This SDK provides Python interfaces to interact with Wangsu API services.

## Installation

Install the SDK using pip:

```bash
pip install wangsu-sdk-python
```

Install the SDK for a specific product category using pip:

```bash
pip install wangsu-sdk-python-ngcertificate
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
from wangsu.ngcertificate.models import *

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
| CreateACertificate | Create a certificate along with its first version. You can choose to upload the key/certificate pair or generate a self-signed one. | POST | /cdn/certificates |
| GetListOfCertificates | Get a list of available certificates including each certificate's ID, name, version deployed to production, version deployed to staging, the latest version number, when the certificate was last updated, and when the certificate expires. By default, certificates are returned in order of most recently updated first. Use query parameters to filter the list of returned certificates. | GET | /cdn/certificates |
| GetACertificate | Gets details about a certificate including the versions of the certificate and who is using it. | GET | /cdn/certificates/* |
| UpdateACertificate | UpdateACertificate using this API. The fields are the same as those in the <a href="#operation/createCertificate">Create a certificate API</a>. If the certificate is currently used by properties deployed to production or staging, we recommend that you follow this API call by <a href="#operation/createDeployment">creating a deployment task</a> to deploy the updated certificate. Otherwise, CDN Pro may still serve content using an older version of the certificate. | PATCH | /cdn/certificates/* |
| DeleteACertificate | This API lets you delete a certificate that is not being used in production or staging. | DELETE | /cdn/certificates/* |
| DownloadTheCsr | Obtain the certificate signing request (CSR) information. You can take it to a certificate authority to apply for a certificate. Once you have it, you should update our system using the 'Update a certificate' API. | GET | /cdn/certificates/*/csr |
| GetACertificateVersionsDetails | Obtain details about a certificate version including the expiration date, algorithm and key length, fingerprint, and whether it is deployed in production and staging. | GET | /cdn/certificates/*/versions/* |