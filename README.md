[![Downloads](https://static.pepy.tech/badge/kendama)](https://pepy.tech/project/kendama)

# kendama
国税庁が提供するインボイス制度適格請求書発行事業者公表システムWeb-APIを使用するためのクライアントAPI(https://www.invoice-kohyo.nta.go.jp/web-api/index.html)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 0.1.3
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

Requests is available on PyPI:

```sh
pip install kendama
```

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/uichi/kendama-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/uichi/kendama-python.git`)

Then import the package:
```python
import kendama
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import kendama
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import kendama
from kendama.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://kensyo.invoice-kohyo.nta.go.jp
# See configuration.py for a list of all supported configuration parameters.
configuration = kendama.Configuration(
    host = "https://kensyo.invoice-kohyo.nta.go.jp"
)



# Enter a context with an instance of the API client
with kendama.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kendama.V1Api(api_client)
    id = 'id_example' # str | 
    var_from = 'Tue Oct 01 09:00:00 JST 2024' # date | 
    to = 'Tue Oct 01 09:00:00 JST 2024' # date | 
    type = '21' # str |  (default to '21')
    division = '1' # str |  (optional) (default to '1')
    divide = '1' # str |  (optional) (default to '1')

    try:
        # 取得期間を指定して情報を取得
        api_response = api_instance.get_announcement_by_diff(id, var_from, to, type, division=division, divide=divide)
        print("The response of V1Api->get_announcement_by_diff:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V1Api->get_announcement_by_diff: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://kensyo.invoice-kohyo.nta.go.jp*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*V1Api* | [**get_announcement_by_diff**](docs/V1Api.md#get_announcement_by_diff) | **GET** /1/diff | 取得期間を指定して情報を取得
*V1Api* | [**get_announcement_by_number**](docs/V1Api.md#get_announcement_by_number) | **GET** /1/num | 登録番号を指定して情報を取得
*V1Api* | [**get_announcement_by_valid**](docs/V1Api.md#get_announcement_by_valid) | **GET** /1/valid | 登録番号と日付を指定して情報を取得


## Documentation For Models

 - [Announcement](docs/Announcement.md)
 - [ResponseBody](docs/ResponseBody.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author
- [uichi](https://github.com/uichi)
