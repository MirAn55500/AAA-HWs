from unittest.mock import patch
from what_is_year_now import what_is_year_now


def test_get_cases():
    with patch('urllib.request.urlopen') as mocked_get_cases:
        mocked_response = mocked_get_cases.return_value

        json_data = '{"currentDateTime": "2023-11-01"}'
        mocked_response.__enter__.return_value.read.return_value = json_data
        assert what_is_year_now() == 2023, 'test 1 failed'

        json_data = '{"currentDateTime": "01.03.2023"}'
        mocked_response.__enter__.return_value.read.return_value = json_data
        assert what_is_year_now() == 2023, 'test 2 failed'

        json_data = '{"currentDateTime": "01-11-2023"}'
        mocked_response.__enter__.return_value.read.return_value = json_data
        try:
            what_is_year_now()
        except ValueError:
            pass
        else:
            print('test 3 failed')


if __name__ == "__main__":
    test_get_cases
