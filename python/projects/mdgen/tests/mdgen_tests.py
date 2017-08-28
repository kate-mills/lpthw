from nose.tools import *
from mdgen import utils
import re


def test_troll_directories():
    # given a directory, return all of its contents
    results = utils.trolls_directories('.')
    # assert that we have the same contents
    assert_true('./NOTES' in results)


def teardown():
    print "TEAR DOWN!"


def test_basic():
    print "I RAN!"
