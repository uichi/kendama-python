# kendama.V1Api

All URIs are relative to *https://kensyo.invoice-kohyo.nta.go.jp*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_announcement_by_diff**](V1Api.md#get_announcement_by_diff) | **GET** /1/diff | 取得期間を指定して情報を取得
[**get_announcement_by_number**](V1Api.md#get_announcement_by_number) | **GET** /1/num | 登録番号を指定して情報を取得
[**get_announcement_by_valid**](V1Api.md#get_announcement_by_valid) | **GET** /1/valid | 登録番号と日付を指定して情報を取得


# **get_announcement_by_diff**
> ResponseBody get_announcement_by_diff(id, var_from, to, type, division=division, divide=divide)

取得期間を指定して情報を取得

取得期間を指定し、当該期間内に「更新年月日」が含まれる公表情報を取得

### Example

```python
import time
import os
import kendama
from kendama.models.response_body import ResponseBody
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
    except Exception as e:
        print("Exception when calling V1Api->get_announcement_by_diff: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **var_from** | **date**|  | 
 **to** | **date**|  | 
 **type** | **str**|  | [default to &#39;21&#39;]
 **division** | **str**|  | [optional] [default to &#39;1&#39;]
 **divide** | **str**|  | [optional] [default to &#39;1&#39;]

### Return type

[**ResponseBody**](ResponseBody.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_announcement_by_number**
> ResponseBody get_announcement_by_number(id, number, type, history=history)

登録番号を指定して情報を取得

指定された登録番号に係る登録年月日、取消年月日及び失効年月日に紐づく最新情報（履歴情報は任意）を取得

### Example

```python
import time
import os
import kendama
from kendama.models.response_body import ResponseBody
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
    number = 'T8040001999011' # str | 
    type = '21' # str |  (default to '21')
    history = '0' # str |  (optional)

    try:
        # 登録番号を指定して情報を取得
        api_response = api_instance.get_announcement_by_number(id, number, type, history=history)
        print("The response of V1Api->get_announcement_by_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->get_announcement_by_number: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **number** | **str**|  | 
 **type** | **str**|  | [default to &#39;21&#39;]
 **history** | **str**|  | [optional] 

### Return type

[**ResponseBody**](ResponseBody.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_announcement_by_valid**
> ResponseBody get_announcement_by_valid(id, number, day, type)

登録番号と日付を指定して情報を取得

登録番号及び指定された日付を基準日とした直近の登録年月日、取消年月日、失効年月日に紐づく情報を取得

### Example

```python
import time
import os
import kendama
from kendama.models.response_body import ResponseBody
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
    number = 'T8040001999011' # str | 
    day = 'Fri Dec 01 09:00:00 JST 2023' # date | 
    type = '21' # str |  (default to '21')

    try:
        # 登録番号と日付を指定して情報を取得
        api_response = api_instance.get_announcement_by_valid(id, number, day, type)
        print("The response of V1Api->get_announcement_by_valid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->get_announcement_by_valid: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **number** | **str**|  | 
 **day** | **date**|  | 
 **type** | **str**|  | [default to &#39;21&#39;]

### Return type

[**ResponseBody**](ResponseBody.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

