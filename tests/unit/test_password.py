"""
    tests for password class
"""
import re
import pytest

import password

def test_retrieve_word_list(mocker):
    """ simple test to check that wordlist is being populated """
    pswd = password.Password()
    assert len(pswd.word_list) > 0

def test_generate_pswd():
    num_words = 5
    pswd = password.Password()
    pswd.generate_pswd(num_words)
    pattern = re.compile(r"[a-zA-Z0-9]\!\"$%&\(\)\*\+\-:;=\?@")
    uppers = pattern.findall(pswd.password)
    print(pswd.password)
    print(uppers)
    assert uppers is None