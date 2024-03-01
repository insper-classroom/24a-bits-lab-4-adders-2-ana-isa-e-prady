#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

from myhdl import *


@block
def halfAdder(a, b, soma, carry):
    @always_comb
    def comb():
        # soma = Signal(bool(0))
        # carry = Signal(bool(0))

        soma.next = ((not a ) and b) or (a and (not b))
        carry.next = a and b 

    return instances()


@block
def fullAdder(a, b, c, soma, carry):
    s = [Signal(bool(0)) for i in range(3)]

    # s1 = Signal(bool(0))
    # s2 = Signal(bool(0))
    # s3 =Signal(bool(0))

    half1 = halfAdder(a, b, s[0], s[1])
    half2 = halfAdder(c, s[0], soma, s[2])

    @always_comb
    def comb():
        carry.next = s[1] or s[2]

    return instances()


@block
def adder2bits(x, y, soma, carry):
    c = Signal(bool(0))
    half = halfAdder(x[0], y[0], soma[0], c)
    
    full = fullAdder(x[1], y[1], c, soma[1], carry)

    return instances()


@block
def adder(x, y, soma, carry):
    @always_comb
    def comb():
        pass

    return instances()
