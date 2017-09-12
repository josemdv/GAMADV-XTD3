# -*- coding: utf-8 -*-

# Copyright (C) 2016 Ross Scroggs All Rights Reserved.
#
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""GAM messages

"""

# These values can be translated into other languages
ACCESS_FORBIDDEN = u'Access Forbidden'
ACTION_APPLIED = u'Action Applied'
ADMIN_STATUS_CHANGED_TO = u'Admin Status Changed to'
ALL = u'All'
ALREADY_EXISTS_USE_MERGE_ARGUMENT = u'Already exists; use the "merge" argument to merge the labels'
API_ACCESS_DENIED = u'API access Denied.\nPlease make sure the Client ID: {0} is authorized for the appropriate scopes {1}'
API_ERROR_SETTINGS = u'API error, some settings not set'
ARE_MUTUALLY_EXCLUSIVE = u'arguments {0} and {1} are mutually exclusive'
AS = u'as'
BAD_REQUEST = u'Bad Request'
BATCH = u'Batch'
BATCH_CSV_LOOP_DASH_DEBUG_INCOMPATIBLE = u'"gam {0} - ..." is not compatible with debugging. Disable debugging by setting debug_level = 0 in gam.cfg'
BATCH_NOT_PROCESSED_ERRORS = u'{0}batch file: {1}, not processed, {2} {3}\n'
CAN_NOT_BE_DOWNLOADED = u'Can not be downloaded'
COMMIT_BATCH_COMPLETE = u'commit-batch - running {0} finished, proceeding\n'
COMMIT_BATCH_WAIT_N_PROCESSES = u'commit-batch - waiting for {0} running {1} to finish before proceeding\n'
CONTAINS_AT_LEAST_1_ITEM = u'Contains at least 1 item'
COUNT_N_EXCEEDS_MAX_TO_PROCESS_M = u'Count {0} exceeds maximum to {1} {2}'
CREATE_USER_NOTIFY_MESSAGE = u'Hello #givenname# #familyname#,\n\nYou have a new account at #domain#\nAccount details:\n\nUsername\n#user#\n\nPassword\n#password#\n\nStart using your new account by signing in at\nhttps://www.google.com/accounts/AccountChooser?Email=#user#&continue=https://apps.google.com/user/hub\n'
CREATE_USER_NOTIFY_SUBJECT = u'Welcome to #domain#'
CSV_DATA_ALREADY_SAVED = u'CSV data already saved'
DATA_FIELD_MISMATCH = u'datafield {0} does not match saved datafield {1}'
DATA_UPLOADED_TO_DRIVE_FILE = u'Data uploaded to Drive File'
DIRECTLY_IN_THE = u' directly in the {0}'
DOES_NOT_EXIST = u'Does not exist'
DOES_NOT_EXIST_OR_HAS_INVALID_FORMAT = u'{0}: {1}, Does not exist or has invalid format'
DOMAIN_NOT_VERIFIED_SECONDARY = u'Domain is not a verified secondary domain'
DO_NOT_EXIST = u'Do not exist'
DUPLICATE = u'Duplicate'
EITHER = u'Either'
ENTITY_DOES_NOT_EXIST = u'{0} does not exist'
ENTITY_NAME_NOT_VALID = u'Entity Name Not Valid'
ERROR = u'error'
ERRORS = u'errors'
EXECUTE_GAM_OAUTH_CREATE = u'\nPlease execute "gam oauth create"\n'
EXISTS = u'Exists'
EXPECTED = u'Expected'
FAILED_TO_PARSE_AS_JSON = u'Failed to parse as JSON'
FIELD_NOT_FOUND_IN_SCHEMA = u'Field {0} not found in schema {1}'
FINISHED = u'Finished'
FOR = u'for'
FORBIDDEN = u'Forbidden'
FORMAT_NOT_AVAILABLE = u'Format ({0}) not available'
FORMAT_NOT_DOWNLOADABLE = u'Format not downloadable'
FROM = u'From'
GAM_EXITING_FOR_UPDATE = u'GAM is now exiting so that you can overwrite this old version with the latest release'
GAM_OUT_OF_MEMORY = u'GAM has run out of memory. If this is a large G Suite instance, you should use a 64-bit version of GAM on Windows or a 64-bit version of Python on other systems.'
GETTING = u'Getting'
GETTING_ALL = u'Getting all'
GOOGLE_DELEGATION_ERROR = u'Google delegation error, delegator and delegate both exist and are valid for delegation'
GOOGLE_EARLIEST_REPORT_TIME = u'Google earliest report time'
GOT = u'Got'
GUARDIAN_INVITATION_STATUS_NOT_PENDING = u'Guardian invitation status is not PENDING'
HAS_CHILD_ORGS = u'Has child {0}'
HEADER_NOT_FOUND_IN_CSV_HEADERS = u'Header "{0}" not found in CSV headers of "{1}".'
HELP_SYNTAX = u'Help: Syntax in file {0}\n'
HELP_WIKI = u'Help: Documentation is at {0}\n'
HIT_CONTROL_C_TO_UPDATE = u'\n\nHit CTRL+C to visit the GAM website and download the latest release or wait 15 seconds continue with this boring old version. GAM won\'t bother you with this announcement for 1 week or you can turn off update checks by setting no_update_check = true in gam.cfg'
IGNORED = u'Ignored'
IN_THE = u' in the {0}'
INSTRUCTIONS_CHECK_AUTHORIZATIONS = u'Please run\n\ngam oauth info\ngam user <user> check serviceaccount\n\nto verify authorizations.\n'
INSTRUCTIONS_CLIENT_SECRETS_JSON = u'Please run\n\ngam create project\ngam oauth create\n\nto create and authorize a Client account.\n'
INSTRUCTIONS_OAUTH2SERVICE_JSON = u'Please run\n\ngam create project\ngam user <user> check serviceaccount\n\nto create and authorizee a Service account.\n'
INSUFFICIENT_PERMISSIONS_TO_PERFORM_TASK = u'Insufficient permissions to perform this task'
INVALID = u'Invalid'
INVALID_ALIAS = u'Invalid Alias'
INVALID_ENTITY_MESSAGE = u'Invalid {0}, {1}'
INVALID_GROUP = u'Invalid Group'
INVALID_JSON_INFORMATION = u'Google API reported Invalid JSON Information'
INVALID_MESSAGE_ID = u'Invalid message id(s)'
INVALID_ORGUNIT = u'Invalid Organizational Unit'
INVALID_OWNER_TYPE = u'role {0} not allowed with {1}'
INVALID_PATH = u'Invalid Path'
INVALID_QUERY = u'Invalid Query'
INVALID_REQUEST = u'Invalid Request'
INVALID_ROLE = u'Invalid Role'
INVALID_SCHEMA_VALUE = u'Invalid Schema Value'
INVALID_SCOPE = u'Invalid Scope'
INVALID_SITE = u'Invalid Site ({0}), must match pattern ({1})'
INVALID_TIME_RANGE = u'{0} {1} must be greater than/equal to {2} {3}'
IS_NOT_UNIQUE = u'Is not unique, {0}: {1}'
IS_REQD_TO_CHG_PWD_NO_DELEGATION = u'Is required to change password at next login. You must change password or clear changepassword flag for delegation.'
IS_SUSPENDED_NO_DELEGATION = u'Is suspended. You must unsuspend for delegation.'
LOOKING_UP_GOOGLE_UNIQUE_ID = u'Looking up Google Unique ID'
MARKED_AS = u'Marked as'
MATCHED_THE_FOLLOWING = u'Matched the following'
MAXIMUM_OF = u'maximum of'
MAY_TAKE_SOME_TIME_ON_A_LARGE = u'may take some time on a large'
MISMATCH_RE_SEARCH_REPLACE_SUBFIELDS = u'The subfield ({2}) in replace "{3}" exceeds the number of subfields ({0}) in search "{1}"'
MISMATCH_SEARCH_REPLACE_SUBFIELDS = u'The number of subfields ({0}) in search "{1}" does not match the number of subfields ({2}) in replace "{3}"'
NESTED_LOOP_CMD_NOT_ALLOWED = u'Command can not be nested.'
NEW_OWNER_MUST_DIFFER_FROM_OLD_OWNER = u'New owner must differ from old owner'
NON_BLANK = u'Non-blank'
NON_EMPTY = u'Non-empty'
NOT_A = u'Not a'
NOT_ALLOWED = u'Not Allowed'
NOT_AN_ENTITY = u'Not a {0}'
NOT_FOUND = u'Not Found'
NOT_OWNED_BY = u'Not owned by {0}'
NOT_WRITABLE = u'Not Writable'
NOW_THE_PRIMARY_DOMAIN = u'Now the primary domain'
NO_CSV_FILE_DATA_SAVED = u'No CSV file data saved'
NO_CSV_FILE_SUBKEYS_SAVED = u'No CSV file subkeys saved'
NO_ENTITIES_FOUND = u'No {0} found'
NO_ENTITIES_MATCHED = u'No {0} matched'
NO_FILTER_ACTIONS = u'No {0} actions specified'
NO_FILTER_CRITERIA = u'No {0} criteria specified'
NO_LABELS_MATCH = u'No Labels match'
NO_MESSAGES_WITH_LABEL = u'No Messages with Label'
NO_PRINT_JOBS = u'No Print Jobs'
NO_PYTHON_SSL = u'You don\'t have the Python SSL module installed so we can\'t verify SSL Certificates. You can fix this by installing the Python SSL module or you can live on the edge and turn SSL validation off by setting no_verify_ssl = true in gam.cfg'
NO_REPORT_AVAILABLE = u'No {0} report available.'
NO_SCOPES_FOR_API = u'There are no scopes authorized for the {0}'
NO_TRANSFER_LACK_OF_DISK_SPACE = u'Cowardly refusing to perform migration due to lack of target drive space.'
NO_USER_COUNTS_DATA_AVAILABLE = u'No User counts data available.'
ONLY_ONE_OWNER_ALLOWED = u'Only one owner allowed'
OR = u'or'
PLEASE_SELECT_ENTITY_TO_PROCESS = u'{0} {1} found, please select the correct one to {2} and specify with {3}'
PREVIEW_ONLY = u'Preview Only'
PROCESS = u'process'
PROCESSES = u'processes'
PROCESSING_ITEM_N = u'Processing item {0}\n'
REFUSING_TO_DEPROVISION_DEVICES = u'Refusing to deprovision {0} devices because acknowledge_device_touch_requirement not specified.\nDeprovisioning a device means the device will have to be physically wiped and re-enrolled to be managed by your domain again.\nThis requires physical access to the device and is very time consuming to perform for each device.\nPlease add "acknowledge_device_touch_requirement" to the GAM command if you understand this and wish to proceed with the deprovision.\nPlease also be aware that deprovisioning can have an effect on your device license count.\nSee https://support.google.com/chrome/a/answer/3523633 for full details.'
REQUEST_COMPLETED_NO_FILES = u'Request completed but no results/files were returned, try requesting again'
REQUEST_NOT_COMPLETE = u'Request needs to be completed before downloading, current status is: {0}'
RESULTS_TOO_LARGE_FOR_GOOGLE_SPREADSHEET = u'Results are too large for Google Spreadsheets. Uploading as a regular CSV file.'
SCHEMA_WOULD_HAVE_NO_FIELDS = u'{0} would have no {1}'
SCOPE_AUTHORIZATION_FAILED = u'Some scopes failed! Please go to:\n\nhttps://admin.google.com/{0}/AdminHome?#OGX:ManageOauthClients\n\nand grant Service Account Client name:\n\n{1}\n\nAccess to scopes:\n\n{2}'
SCOPE_AUTHORIZATION_PASSED = u'All scopes passed!\nService Account Client name {0} is fully authorized.'
SELECTED = u'Selected'
SERVICE_NOT_APPLICABLE_THIS_ADDRESS = u'Service not applicable for this address: {0}'
SERVICE_NOT_APPLICABLE = u'Service not applicable/Does not exist'
SKU_PRODUCT_MISMATCH = u'Product {0} of old SKU does not match product {1} of new SKU'
STARTING_THREAD = u'Starting thread'
STRING_LENGTH = u'string length'
SUBKEY_FIELD_MISMATCH = u'subkeyfield {0} does not match saved subkeyfield {1}'
SUBSCRIPTION_NOT_FOUND = u'Could not find subscription'
THAT_MATCHED_QUERY = u'that matched query'
THAT_MATCH_QUERY = u'that match query'
THREAD = u'thread'
THREADS = u'threads'
TO = u'To'
UNAVAILABLE = u'Unavailable'
UNKNOWN = u'Unknown'
UNKNOWN_API_OR_VERSION = u'Unknown Google API or version: ({0}), contact {1}'
UNKNOWN_COMMAND_SELECTOR = u'Unknown command or selector'
USER_IN_OTHER_DOMAIN = u'{0}: {1} in other domain.'
USE_DOIT_ARGUMENT_TO_PERFORM_ACTION = u'Use the "doit" argument to perform action'
USE_RECURSIVE_ARGUMENT_TO_COPY_FOLDERS = u'Use "recursive" argument to copy folders'
USING_N_PROCESSES = u'Using {0} {1}...\n'
WITH = u'with'
WITHLINK_INCOMPATIBILITY = u'withlink/allowfilediscovery not compatible with role type {0}'
WOULD_MAKE_MEMBERSHIP_CYCLE = u'Would make membership cycle'
