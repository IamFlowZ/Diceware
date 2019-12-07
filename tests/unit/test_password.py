"""
    tests for password class
"""
import re
import pytest

import password

def test_retrieve_word_list(mocker):
    """ check that wordlist is being populated """
    pswd = password.Password()
    assert len(pswd.word_list) > 0

def test_no_sources(mocker):
    """ fudging the path in order to simulate the file not exisiting. """
    open_mock = mocker.patch('os.getcwd')
    open_mock.return_value = '/'
    try:
        password.Password()
    except FileNotFoundError as e:
        assert str(e) == 'Please install the dicelist sources.'

def test_generate_pswd():
    """ generated passwords should be at least as long as the number of words provided """
    num_words = 5
    pswd = password.Password()
    pswd.generate_pswd(num_words)
    assert len(pswd.password) >= 5

@pytest.mark.skip(reason="not done")
def test_replace_char():
    pswd = password.Password()
    pswd.generate_pswd()