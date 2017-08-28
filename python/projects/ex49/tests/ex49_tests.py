from nose.tools import *
from ex49.parser import *


def test_Sentence():
  x = [('noun', 'princess'), ('verb', 'run'), ('direction', 'north')]
  player = Sentence(x[0], x[1], x[2])
  assert_equal(player.subject, "princess")
  assert_equal(player.verb, "run")
  assert_equal(player.object, "north")


def test_peek():
  pass


def test_match():
  pass


def test_skip():
  pass


def test_parse_verb():
  pass


def test_object():
  pass


def test_parse_subject():
  pass


def test_parse_sentence():
  x.subj = "player"
  x.verb = "run"
  x.obj = "north"
