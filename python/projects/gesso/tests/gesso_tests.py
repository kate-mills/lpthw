from nose.tools import *
from gesso import acrylic
from gesso import oil


def setup():
  print "SETUP!"


def teardown():
  print "TEAR DOWN!"


def test_basic():
  print "I RAN!"


def test_paint():
  acrylic.paint("blue")


def test_paint_canvas():
  oil.paint_canvas("blue")


def test_paint_board():
  oil.paint_board("mixed media", "red")
