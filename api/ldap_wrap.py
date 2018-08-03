#!/usr/bin/env python3

from ldap3 import Server, Connection, ALL


def slapd_port():
    """local port used by the slapd
    """
    return "8888"


def ldap_host():
    """host provided to the Server definition
    """
    return "0.0.0.0:{}".format(slapd_port())


def ldap_ssl():
    """use of ssl for the Server definition
    """
    return False


def ldap_infolevel():
    """level of info queried to the Server
    """
    return 'SCHEMA'


def ldap_autobind():
    """use of autobind for a Connection
    """
    return False


def ldap_binduser():
    """account dn used for binding
    """
    return 'uid=admin,cn=users'


def ldap_bindpwd():
    """password used for binding
    """
    return 'Secret123'


def ldap_server():
    """definition of a LDAP Server
    """
    return Server(ldap_host(),
                  use_ssl=ldap_ssl(),
                  get_info=ldap_infolevel(),
                  )


def ldap_creds(anon=False):
    if anon:
        return (None, None)
    else:
        return (ldap_binduser(), ldap_bindpwd())


def ldap_conn(anon=False):
    """setup of a Connection
    """
    creds = ldap_creds(anon)
    return Connection(ldap_server(),
                      creds[0],
                      creds[1],
                      auto_bind=ldap_autobind(),
                      )
