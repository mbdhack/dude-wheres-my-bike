TIME_ZONE = 'America/New_York'
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# The SHAREABOUTS['FLAVOR'] environment variable is used as a prefix for the
# Shareabouts configuration. configuration is expected to live in a package
# named 'flavors.<SHAREABOUTS_FLAVOR>'. This package will correspond to a
# folder in the root of the src tree that contains all the configuration
# information for the flavor.

SHAREABOUTS = {
  'FLAVOR': 'dudewheresmybike',
  #'FLAVOR': 'default_config',
  'DATASET_ROOT': 'http://api.shareabouts.org/api/v1/codeformiami/datasets/dwmb/',
  'DATASET_KEY': 'NWQyMGE2MDljZDBjOTI4ZTViNTZhNDEz',
}

# SHAREABOUTS = {
#   'FLAVOR': 'default_config',
#   'DATASET_ROOT': 'http://api.shareabouts.org/api/v1/demo-user/datasets/demo-data/',
#   'DATASET_KEY': 'abc123',
# }

#SHAREABOUTS = {
#  'FLAVOR': 'bikeparking',
#  'DATASET_ROOT': 'http://api.shareabouts.org/api/v1/openplans/datasets/rr-stations/',
#  'DATASET_KEY': 'abc123',
#}

#SHAREABOUTS = {
#  'FLAVOR': 'biketotransit',
#  'DATASET_ROOT': 'http://api.shareabouts.org/api/v1/biketotransit/datasets/biketotransit/',
#  'DATASET_KEY': 'abc123',
#}

#SHAREABOUTS = {
#  'FLAVOR': 'communitymap',
#  'DATASET_ROOT': 'http://api.shareabouts.org/api/v1/openplans/datasets/community-map/',
#  'DATASET_KEY': 'abc123',
#}

#SHAREABOUTS = {
#  'FLAVOR': 'historiclouisville',
#  'DATASET_ROOT': 'http://api.shareabouts.org/api/v1/historiclouisville/datasets/historiclouisville/',
#  'DATASET_KEY': 'abc123',
#}

#SHAREABOUTS = {
#  'FLAVOR': 'jacksonheights',
#  'DATASET_ROOT': 'http://api.shareabouts.org/api/v1/jacksonheights/datasets/jacksonheights/',
#  'DATASET_KEY': 'abc123',
#}

#SHAREABOUTS = {
#  'FLAVOR': 'makebrooklynsafer',
#  'DATASET_ROOT': 'http://api.shareabouts.org/api/v1/makebrooklynsafer/datasets/makebrooklynsafer/',
#  'DATASET_KEY': 'abc123',
#}

#SHAREABOUTS = {
#  'FLAVOR': 'nosur',
#  'DATASET_ROOT': 'http://api.shareabouts.org/api/v1/openplans/datasets/atm_surcharge/',
#  'DATASET_KEY': 'abc123',
#}

#SHAREABOUTS = {
#  'FLAVOR': 'overlays',
#  'DATASET_ROOT': 'http://api.shareabouts.org/api/v1/demo-user/datasets/demo-data/',
#  'DATASET_KEY': 'abc123',
#}

#SHAREABOUTS = {
#  'FLAVOR': 'ped_obstacles',
#  'DATASET_ROOT': 'http://api.shareabouts.org/api/v1/openplans/datasets/ped_obstacles/',
#  'DATASET_KEY': 'abc123',
#}

#SHAREABOUTS = {
#  'FLAVOR': 'sistercities',
#  'DATASET_ROOT': 'http://api.shareabouts.org/api/v1/openplans/datasets/sc-usage/',
#  'DATASET_KEY': 'abc123',
#}

#SHAREABOUTS = {
#  'FLAVOR': 'urbansocial',
#  'DATASET_ROOT': 'http://api.shareabouts.org/api/v1/urbansocial/datasets/urbansocial/',
#  'DATASET_KEY': 'abc123',
#}
