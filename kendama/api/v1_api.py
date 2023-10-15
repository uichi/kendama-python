# coding: utf-8

"""
    国税庁API

    国税庁が提供するインボイス制度適格請求書発行事業者公表システムWeb-APIを使用するためのクライアントAPI(https://www.invoice-kohyo.nta.go.jp/web-api/index.html)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from datetime import date

from pydantic import StrictStr, constr

from typing import Optional

from kendama.models.response_body import ResponseBody

from kendama.api_client import ApiClient
from kendama.api_response import ApiResponse
from kendama.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class V1Api:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_announcement_by_diff(self, id : StrictStr, var_from : date, to : date, type : StrictStr, division : Optional[StrictStr] = None, divide : Optional[constr(strict=True, max_length=999999, min_length=1)] = None, **kwargs) -> ResponseBody:  # noqa: E501
        """取得期間を指定して情報を取得  # noqa: E501

        取得期間を指定し、当該期間内に「更新年月日」が含まれる公表情報を取得  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_announcement_by_diff(id, var_from, to, type, division, divide, async_req=True)
        >>> result = thread.get()

        :param id: (required)
        :type id: str
        :param var_from: (required)
        :type var_from: date
        :param to: (required)
        :type to: date
        :param type: (required)
        :type type: str
        :param division:
        :type division: str
        :param divide:
        :type divide: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ResponseBody
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_announcement_by_diff_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_announcement_by_diff_with_http_info(id, var_from, to, type, division, divide, **kwargs)  # noqa: E501

    @validate_arguments
    def get_announcement_by_diff_with_http_info(self, id : StrictStr, var_from : date, to : date, type : StrictStr, division : Optional[StrictStr] = None, divide : Optional[constr(strict=True, max_length=999999, min_length=1)] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """取得期間を指定して情報を取得  # noqa: E501

        取得期間を指定し、当該期間内に「更新年月日」が含まれる公表情報を取得  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_announcement_by_diff_with_http_info(id, var_from, to, type, division, divide, async_req=True)
        >>> result = thread.get()

        :param id: (required)
        :type id: str
        :param var_from: (required)
        :type var_from: date
        :param to: (required)
        :type to: date
        :param type: (required)
        :type type: str
        :param division:
        :type division: str
        :param divide:
        :type divide: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ResponseBody, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'id',
            'var_from',
            'to',
            'type',
            'division',
            'divide'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_announcement_by_diff" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('id') is not None:  # noqa: E501
            _query_params.append(('id', _params['id']))

        if _params.get('var_from') is not None:  # noqa: E501
            if isinstance(_params['var_from'], date):
                _query_params.append(('from', _params['var_from'].strftime(self.api_client.configuration.date_format)))
            else:
                _query_params.append(('from', _params['var_from']))

        if _params.get('to') is not None:  # noqa: E501
            if isinstance(_params['to'], date):
                _query_params.append(('to', _params['to'].strftime(self.api_client.configuration.date_format)))
            else:
                _query_params.append(('to', _params['to']))

        if _params.get('type') is not None:  # noqa: E501
            _query_params.append(('type', _params['type']))

        if _params.get('division') is not None:  # noqa: E501
            _query_params.append(('division', _params['division']))

        if _params.get('divide') is not None:  # noqa: E501
            _query_params.append(('divide', _params['divide']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "ResponseBody",
        }

        return self.api_client.call_api(
            '/1/diff', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_announcement_by_number(self, id : StrictStr, number : StrictStr, type : StrictStr, history : Optional[StrictStr] = None, **kwargs) -> ResponseBody:  # noqa: E501
        """登録番号を指定して情報を取得  # noqa: E501

        指定された登録番号に係る登録年月日、取消年月日及び失効年月日に紐づく最新情報（履歴情報は任意）を取得  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_announcement_by_number(id, number, type, history, async_req=True)
        >>> result = thread.get()

        :param id: (required)
        :type id: str
        :param number: (required)
        :type number: str
        :param type: (required)
        :type type: str
        :param history:
        :type history: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ResponseBody
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_announcement_by_number_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_announcement_by_number_with_http_info(id, number, type, history, **kwargs)  # noqa: E501

    @validate_arguments
    def get_announcement_by_number_with_http_info(self, id : StrictStr, number : StrictStr, type : StrictStr, history : Optional[StrictStr] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """登録番号を指定して情報を取得  # noqa: E501

        指定された登録番号に係る登録年月日、取消年月日及び失効年月日に紐づく最新情報（履歴情報は任意）を取得  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_announcement_by_number_with_http_info(id, number, type, history, async_req=True)
        >>> result = thread.get()

        :param id: (required)
        :type id: str
        :param number: (required)
        :type number: str
        :param type: (required)
        :type type: str
        :param history:
        :type history: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ResponseBody, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'id',
            'number',
            'type',
            'history'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_announcement_by_number" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('id') is not None:  # noqa: E501
            _query_params.append(('id', _params['id']))

        if _params.get('number') is not None:  # noqa: E501
            _query_params.append(('number', _params['number']))

        if _params.get('type') is not None:  # noqa: E501
            _query_params.append(('type', _params['type']))

        if _params.get('history') is not None:  # noqa: E501
            _query_params.append(('history', _params['history']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "ResponseBody",
        }

        return self.api_client.call_api(
            '/1/num', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_announcement_by_valid(self, id : StrictStr, number : StrictStr, day : date, type : StrictStr, **kwargs) -> ResponseBody:  # noqa: E501
        """登録番号と日付を指定して情報を取得  # noqa: E501

        登録番号及び指定された日付を基準日とした直近の登録年月日、取消年月日、失効年月日に紐づく情報を取得  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_announcement_by_valid(id, number, day, type, async_req=True)
        >>> result = thread.get()

        :param id: (required)
        :type id: str
        :param number: (required)
        :type number: str
        :param day: (required)
        :type day: date
        :param type: (required)
        :type type: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ResponseBody
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_announcement_by_valid_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_announcement_by_valid_with_http_info(id, number, day, type, **kwargs)  # noqa: E501

    @validate_arguments
    def get_announcement_by_valid_with_http_info(self, id : StrictStr, number : StrictStr, day : date, type : StrictStr, **kwargs) -> ApiResponse:  # noqa: E501
        """登録番号と日付を指定して情報を取得  # noqa: E501

        登録番号及び指定された日付を基準日とした直近の登録年月日、取消年月日、失効年月日に紐づく情報を取得  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_announcement_by_valid_with_http_info(id, number, day, type, async_req=True)
        >>> result = thread.get()

        :param id: (required)
        :type id: str
        :param number: (required)
        :type number: str
        :param day: (required)
        :type day: date
        :param type: (required)
        :type type: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ResponseBody, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'id',
            'number',
            'day',
            'type'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_announcement_by_valid" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('id') is not None:  # noqa: E501
            _query_params.append(('id', _params['id']))

        if _params.get('number') is not None:  # noqa: E501
            _query_params.append(('number', _params['number']))

        if _params.get('day') is not None:  # noqa: E501
            if isinstance(_params['day'], date):
                _query_params.append(('day', _params['day'].strftime(self.api_client.configuration.date_format)))
            else:
                _query_params.append(('day', _params['day']))

        if _params.get('type') is not None:  # noqa: E501
            _query_params.append(('type', _params['type']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "ResponseBody",
        }

        return self.api_client.call_api(
            '/1/valid', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
