# coding: utf-8

"""
    国税庁API

    国税庁が提供するインボイス制度適格請求書発行事業者公表システムWeb-APIを使用するためのクライアントAPI(https://www.invoice-kohyo.nta.go.jp/web-api/index.html)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.response_body import ResponseBody  # noqa: E501

class TestResponseBody(unittest.TestCase):
    """ResponseBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResponseBody:
        """Test ResponseBody
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResponseBody`
        """
        model = ResponseBody()  # noqa: E501
        if include_optional:
            return ResponseBody(
                last_update_date = 'Mon Nov 01 09:00:00 JST 2021',
                count = '1',
                divide_number = '1',
                divide_size = '1',
                announcement = [
                    openapi_client.models.announcement.Announcement(
                        sequence_number = '1', 
                        registrated_number = 'T8040001999011', 
                        process = '1', 
                        correct = '0', 
                        kind = '2', 
                        country = '1', 
                        latest = '1', 
                        registration_date = 'Sun Oct 01 09:00:00 JST 2023', 
                        update_date = 'Mon Nov 01 09:00:00 JST 2021', 
                        disposal_date = '', 
                        expire_date = '', 
                        address = '北海道札幌市中央区大通西１０丁目', 
                        address_prefecture_code = '1', 
                        address_city_code = '101', 
                        address_request = '', 
                        address_request_prefecture_code = '', 
                        address_request_city_code = '', 
                        kana = '', 
                        name = '株式会社インボイス公表', 
                        address_inside = '', 
                        address_inside_prefecture_code = '', 
                        address_inside_city_code = '', 
                        trade_name = '', 
                        popular_name_previous_name = '', )
                    ]
            )
        else:
            return ResponseBody(
        )
        """

    def testResponseBody(self):
        """Test ResponseBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()