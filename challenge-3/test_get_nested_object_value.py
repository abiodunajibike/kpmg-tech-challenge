import pytest
from unittest import mock
import get_nested_object_value


@pytest.mark.parametrize(
    'object_key',
    [
        ('/a/b/c'),
        ('$a/b/c'),
        ('(a/b/c'),
        ('a/b/c/'),
        ('a/b/c$'),
        ('a/b/c)'),
    ]
)
def test_is_object_key_valid_raises_exception(object_key):

    with pytest.raises(
        get_nested_object_value.ObjectKeyStartsOrEndsWithUnexpectedChar
    ):
        get_nested_object_value.is_object_key_valid(object_key)


@pytest.mark.parametrize(
    'nested_object, object_key, expected_result',
    [
        (
            {
                'person': {
                    'name': 'john doe',
                    'age': '20'
                }
            },
            'person/unknown',
            None
        ),
        (
            {
                'person': {
                    'name': 'john doe',
                    'age': '20'
                }
            },
            'person/age',
            '20'
        ),
        (
            {
                'person': {
                    'info': {
                        'name': 'john doe',
                        'age': '20'
                    }
                }
            },
            'person/info/name',
            'john doe'
        ),
        (
            {
                'person': {
                    'info': {
                        'name': 'john doe', 'age': '20',
                        'body': {
                            'bmi': {
                                'height': '1.2m',
                                'weight': '40lbs'
                            }
                        }
                    }
                }
            },
            'person/info/body/bmi/height',
            '1.2m'
        ),
        (
            {
                'person': {
                    'info': {
                        'name': 'john doe', 'age': '20',
                        'body': {
                            'bmi': {
                                'height': '1.2m',
                                'weight': '40lbs'
                            }
                        }
                    }
                }
            },
            'person/info/body/bmi/ratio',
            None
        ),
    ]
)
def test_get_nested_object_value(nested_object, object_key, expected_result):

    response = get_nested_object_value.get_nested_object_val(
        nested_object, object_key
    )

    assert response == expected_result


@mock.patch("get_nested_object_value.get_nested_object_val")
def test_entry_point(mock_get_nested_object_val):
    with mock.patch(
        "get_nested_object_value.argparse.ArgumentParser.parse_args"
    ) as mock_parse_args:

        get_nested_object_value.main()

        mock_parse_args.assert_called()
        mock_get_nested_object_val.assert_called()


@pytest.mark.parametrize("exit_code", [0, -1])
def test_init_exits_with_right_code(exit_code):

    with mock.patch.object(
        get_nested_object_value, "main", return_value=exit_code
    ):
        with mock.patch.object(
            get_nested_object_value, "__name__", "__main__"
        ):
            with mock.patch.object(
                get_nested_object_value.sys, "exit"
            ) as mock_exit:
                get_nested_object_value.init()

                assert mock_exit.call_args[0][0] == exit_code
