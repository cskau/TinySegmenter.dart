#!/usr/bin/env python
# coding: UTF-8

top = '.'
out = './build'

DART_SDK = '~/bin/dart-sdk'
DART_FROGC = DART_SDK + '/bin/frogc'
DART_VM = DART_SDK + '/bin/dart'

def options(opt):
  pass

def configure(cnf):
  cnf.env.DART_SDK = DART_SDK
  cnf.env.DART_FROGC = DART_FROGC
  cnf.env.DART_VM = DART_VM

def build(bld):
  prog = bld(
      rule='${DART_FROGC} ${SRC}',
      source = 'TinySegmenter.dart',
  )
