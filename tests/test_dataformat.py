from chepy import Chepy


def test_base_58_decode():
    assert Chepy("2UDrs31qcWSPi").base_58_decode.output.decode() == "some data"


def test_base_32_encode():
    assert Chepy("some data").base_32_encode.output.decode() == "ONXW2ZJAMRQXIYI="


def test_base_64_encode():
    assert Chepy("some data").base_64_encode.output.decode() == "c29tZSBkYXRh"


def test_base_58_encode():
    assert Chepy("some data").base_58_encode.output.decode() == "2UDrs31qcWSPi"


def test_to_hex():
    assert Chepy("AAA").to_hex.out().decode() == "414141"


def test_hex_to_int():
    assert Chepy("0x123").hex_to_int.output == 291