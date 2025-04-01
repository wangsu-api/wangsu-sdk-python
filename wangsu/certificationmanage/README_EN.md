# Wangsu SDK for Python

This SDK provides Python interfaces to interact with Wangsu API services.

## Installation

Install the SDK using pip:

```bash
pip install wangsu-sdk-python
```

Install the SDK for a specific product category using pip:

```bash
pip install wangsu-sdk-python-certificationmanage
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
from wangsu.certificationmanage.models import *

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
| Querycertificatelist | Check the SSL certificate lists and information, including certificate ID, certificate name, whether it shares or uses the current certificate domain information, etc. | GET | /api/ssl/certificate |
| Getcertificatecontent | get certificate content | GET | /api/ssl/content/*/download |
| Addcertificateservicev2 | Add a new certificate interface, including certificate name, certificate public key (CRT and Ca content merge), certificate key, csrid and commont. | POST | /api/certificate |
| Deletecertificate | Delete a certificate. A certificate cannot be deleted if it is in use. | DELETE | /api/certificate/* |
| Querycertificateinfo | Returns certificate detail by certificate ID. | GET | /api/certificate/* |
| Editcertificatev2 | Re-upload a certificate. | PUT | /api/certificate/* |
| Querycertificatecontent | Query certificate content | GET | /api/certificate/*/content |
| Querycertificaterelateddomains | Query certificate related domains | GET | /api/certificate/*/domain |
| Revokecertificateserviceforwplus | revoke certificate | POST | /api/certificate/revoke |
| Addgmcertificateforwplus | add gm certificate | POST | /api/certificate/gm/add |
| Querydomainmulticertconfig | Query Domain MultiCert Config | GET | /api/config/certificate/v2/* |
| Reissuecertificateforwplus | This interface is used for reissuing certificates. You can reissue the certificate by providing the certificate ID, certificate description, certificate algorithm, verification method, whether it is automatically verified, whether it is automatically deployed, common name, and subject alternate name. When the call is successful, the interface will return the sales order ID. | POST | /api/certificate/reissue |
| Downloadconfirmlettertemplateforwplus | This interface is used to download the "Information Confirmation Letter" template provided by Asia Digital Integrity. Users can input their organizational information and stamp it through the "Information Confirmation Letter" template to verify the authenticity of the information provided by the CA manufacturer.<br> | POST | /api/certificate/download/confirm/letter/template |
| Uploadconfirmletterforwplus | This interface is used to upload the "Information Confirmation Letter". Users can upload organizational information through this interface, which facilitates the certificate CA manufacturer to confirm whether the organizational information is legal.<br> | POST | /api/certificate/upload/confirm/letter |