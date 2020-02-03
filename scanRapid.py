from __future__ import print_function
import time
from rapid7vmconsole.rest import ApiException
from pprint import pprint
import rapid7vmconsole
import base64
import logging
import sys


config = rapid7vmconsole.Configuration(name='Rapid7')
config.username = 'nxadmin'
config.password = 'nxpassword'
config.host = 'https://localhost:3780'
config.verify_ssl = False
config.assert_hostname = False
config.proxy = None
config.ssl_ca_cert = None
config.connection_pool_maxsize = None
config.cert_file = None
config.key_file = None
config.safe_chars_for_path_param = ''

# Logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.INFO)
logger.addHandler(ch)
config.debug = False

auth = "%s:%s" % (config.username, config.password)
auth = base64.b64encode(auth.encode('ascii')).decode()
client = rapid7vmconsole.ApiClient(configuration=config)
client.default_headers['Authorization'] = "Basic %s" % auth
asset_api = rapid7vmconsole.AssetApi(client)
assets = asset_api.get_assets()
override_blackout = false
scan = rapid7vmconsole.AdhocScan()

try:
    # Site Scans
    for a in assets.resources:
        api_response = asset_api.start_scan(a.id, override_blackout=override_blackout, scan=scan)
        pprint(api_response)

except ApiException as e:
    print("Exception when calling ScanApi->start_scan: %s\n" % e)