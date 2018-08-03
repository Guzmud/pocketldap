#!/usr/bin/env python3

import hug

from ldap_wrap import ldap_conn


@hug.cli()
@hug.local()
@hug.get()
def conn_info():
    with ldap_conn(anon=True) as conn:
        return {'conn': str(conn)}

