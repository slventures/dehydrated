#!/usr/bin/env python3

import sys

_, event = sys.argv[0:2]

if event == 'deploy_challenge':
    domain, _, value = sys.argv[2:]
    sub_domain = "_acme-challenge.{}".format(domain.split('.')[0])
    print("Go set a TXT record for '{}' with value '{}'."
          .format(sub_domain, value))
    input("Hit <ENTER> when you're done... ")
else:
    print("Event '{}' is unhandled, shrugging lazily.".format(event))

