#!/usr/bin/env python3

import sys
import random

locat = '/var/lib/hname'
adjfile = '{}/adjectives.txt'.format(locat)
nounfile = '{}/nouns.txt'.format(locat)

def get_hname():
    with open(adjfile, 'r') as f:
        adjectives = [line.strip() for line in f]

    with open(nounfile, 'r') as f:
        nouns = [line.strip() for line in f]

    return '{}-{}'.format(random.choice(adjectives),
                          random.choice(nouns))
