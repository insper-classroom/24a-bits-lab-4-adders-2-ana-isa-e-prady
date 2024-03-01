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
    @always_comb
    def comb():
        pass

    return instances()


@block
def adder2bits(x, y, soma, carry):
    return instances()


@block
def adder(x, y, soma, carry):
    @always_comb
    def comb():
        pass

    return instances()
