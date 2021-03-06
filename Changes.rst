Changes for v4.4.8 (2018-09-27)
===============================

-  Initialize logging in hca.cli.main (#195)

Changes for v4.4.7 (2018-09-26)
===============================

Fix URL regexp in release script

Changes for v4.4.6 (2018-09-26)
===============================

-  Add release sanity checks

Changes for v4.4.1 (2018-09-20)
===============================

-  US 169 Add command line tool for checking upload area or file status
   (#187)

-  adding a backoff factor and retry redirects for api calls. (#184)

-  The life time of a token can be adjusted for authentication sessions.
   (#182)

Changes for v4.2.1 (2018-09-04)
===============================

-  Re-roll 4.2.0 due to a packaging issue.

Changes for v4.2.0 (2018-09-04)
===============================

-  Synchronize access to Swagger definition

-  Enable programmatic SwaggerClient host configuration (#142)

-  Allow for directory and file extension in hca upload files command
   (#174)

-  Restrict Boto3 dependency version range to 1.7.x (#176). Pin
   commonmark to 0.7.x.

-  upload cli parallelization 5x improvement (#155)

-  Add integration tests for SwaggerClient’s code generation methods
   (#109)

-  Help info for parameters appears in cli for upload and download
   (#146)

Changes for v4.1.4 (2018-08-07)
===============================

Fix ``hca upload file`` to work in production enironment again.

Changes for v4.1.3 (2018-08-06)
===============================

-  Use setuptools entry_points instead of scripts

-  Use s3 multipart constants as defined in dcplib (#150)

-  Documentation improvements

Changes for v4.1.2 (2018-07-27)
===============================

Fix ExpiredToken exceptions during ``hca upload file``

Changes for v4.1.1 (2018-07-27)
===============================

-  Update Google auth scopes to match new injected Google scope

-  Refetch DSS API definition weekly (#79) (#139)

-  Supply the required version to dss.upload (#135)


Changes for v4.0.0 (2018-06-20)
===============================

Upload: creds command and Python binding for get\_credentials Upload:
upload areas are now represented by a URI instead of URN DSS: fix
updated files seeping into downloads of older bundles

Changes for v3.5.2 (2018-06-04)
===============================

-  Resolve internal references in Swagger spec (#122)

Changes for v3.5.1 (2018-05-14)
===============================

-  Apply retry policy when fetching Swagger API definition

Changes for v3.5.0 (2018-05-03)
===============================

-  Add HTTP resume to DCP CLI download. (#101)

-  Cap the number of results for test_search (#111)

-  Provide schema for URLs. (#110)

-  Fix handling of enum values in JSON request bodies

Changes for v3.4.6 (2018-04-19)
===============================

-  Fix CLI parsers (#105)

Changes for v3.4.5 (2018-04-02)
===============================

-  Bump pyOpenSSL dependency on Python 2.7 (#102)

Changes for v3.4.4 (2018-04-02)
===============================

-  Fix version inlining

Changes for v3.4.3 (2018-04-02)
===============================

-  Add timeout policy for requests (#100)

-  Retry streaming read errors in bundle download (#98)

Changes for v3.4.2 (2018-03-30)
===============================

-  Retry on read errors. (#97)

Changes for v3.4.1 (2018-03-29)
===============================

-  Fix streaming managed download in DSS CLI

Changes for v3.4.0 (2018-03-29)
===============================

Use prod API endpoint by default

Changes for v3.3.1 (2018-03-15)
===============================

-  Enable Retry-After for HTTP 301 (#96)

-  Switch to checksumming_io from dcplib (#95)

Changes for v3.3.0 (2018-01-25)
===============================

upload: make upload\_service\_api\_url\_template configurable upload:
fix list command to work for areas with many files (#93) Bump tweak
dependency version (#92) Remove spurious line from autodoc file Send
DSS\_FAKE\_504\_PROBABILITY as a header.

Changes for v3.2.0 (2018-01-17)
===============================

Upload: Turn on S3 Transfer Acceleration by default Retry GET requests
(#87) Rename bundle\_id to bundle\_fqid (#86)

Changes for v3.1.1 (2018-01-03)
===============================

-  Add docs for config management options

-  Parameterize program name in Swagger client error message

-  Avoid wedging config when first run is performed offline

Changes for v3.1.0 (2017-12-14)
===============================

-  Use staging DSS by default

-  Fix typevar passthrough to argparse with typing.Optional kwargs

-  Upload: fix typo that prevented CRC32Cs being display in long
   listings

Changes for v3.0.5 (2017-12-06)
===============================

-  Fix handling of argument defaults in command line parsers

Changes for v3.0.4 (2017-12-04)
===============================

-  Fix regression in Upload CLI behavior, part 2

Changes for v3.0.3 (2017-12-04)
===============================

-  Fix regression in Upload CLI behavior

Changes for v3.0.2 (2017-12-04)
===============================

Fix structured exception printing on Python 2.7

Changes for v3.0.1 (2017-12-04)
===============================

-  Fix release

Changes for v3.0.0 (2017-12-04)
===============================

-  Refactor CLI to use new dynamic SwaggerClient utility class

-  Add structured error response data to exceptions

-  Documentation updates

-  New configuration manager

Changes for v2.3.2 (2017-11-21)
===============================

Fix incompatibility with older pip versions

Changes for v2.3.1 (2017-11-10)
===============================

Improved ``hca upload file`` determination of content-type.

Changes for v2.3.0 (2017-11-08)
===============================

More RFC-compliant support of media-type parameters. Upload dcp-type for
files defaults to "data". Fix: "upload list --long" now prints checksums
correctly. Loosen dependency requirements. "hca dss upload" sets S3
content-type when uploading to fake staging area.

Changes for v2.2.0 (2017-11-03)
===============================

New commands/python bindings: hca upload list - list your currently
selected upload area hca upload forget - remove knowledge of an upload
area Additional functionality: hca upload file: New optional argument
--quiet Now sets a dcp-type parameter on Content-Type when uploading.

Changes for v2.1.0 (2017-10-30)
===============================

Expose Python bindings for Upload Service

Changes for v2.0.0 (2017-10-18)
===============================

Rename 'staging' commands 'upload' Format the result, if any, in json if
--json-output is set. (#67)

Changes for v1.1.3 (2017-10-02)
===============================

Documentation updates.


Changes for v1.1.1 (2017-10-01)
===============================

Fix staging area credentials handling

Changes for v1.1.0 (2017-09-30)
===============================

Command: "hca staging select " Command: "hca staging areas" Command:
"hca staging upload <files" Command: "hca staging help"

Changes for v1.0.0 (2017-09-29)
===============================

Use "hca dss " to invoke DSS commands. Hardware DSS to use staging
deployment. Rename hca.api -> hca.dss. Rename query to es\_query (#58).

Changes for v0.11.0 (2017-09-12)
================================

Support async upload (#44)

Changes for v0.10.1 (2017-09-12)
================================

Fix broken mimetype sniffing logic (#51)

Changes for v0.10.0 (2017-08-17)
================================

Let readthedocs publish api spec (#38) Log to stderr and fix
Oauth2Client inputs

Changes for v0.9.5 (2017-08-16)
===============================

Stream printing to console & print bytes Jmackey popup auth Publish
python bindings to readthedocs

Changes for v0.9.3 (2017-08-04)
===============================

Removing popup capability to release functioning package.

Popups weren't working because client\_secrets.json is required and
wasn't being published with the package.

Changes for v0.9.2 (2017-08-04)
===============================

Add client\_secrets.json to MANIFEST directory.

Changes for v0.9.1 (2017-08-04)
===============================

Fix auto-path set Set config to ~/.config/hca/oauth2.json Reconfigure
auth to include sign-in pop-up if in a teletype

Changes for v0.9.0 (2017-08-02)
===============================

Full python binding support for all endpoints: \* bundles \* files \*
search \* subscriptions

CLI integration on top of these python bindings

Changes for v0.7.0 (2017-08-02)
===============================

Full python binding support for all endpoints: \* bundles \* files \*
search \* subscriptions

CLI integration on top of these python bindings

Changes for v0.7.3 (2017-08-01)
===============================

Add kwarg to redirect to different url.

Changes for v0.7.2 (2017-08-01)
===============================

Remove merge conflict lines.

Changes for v0.7.1 (2017-08-01)
===============================

Fix google auth request import

Changes for v0.7.0 (2017-08-01)
===============================

remove sign so I can release v0.7.0 remove tuple comprehension (python3
doesn't like that) Remove cli tests. Python bindings w/ auth and some
testing Autogenerated functions fully working. making abstractions a
package. Upload/Download refactor: Moved upload/download commands to
hca/api/abstractions dir. Release file resources after completed.
Cherry-picked upload-from-s3 changes Testing head\_files. Don't
regenerate python bindings. Templatize relative imports from
autogenerated. Remove unnecessary import Relative imports from
autogenerated Include all jinja files and update tests. Populate test
bundle with real data avoid namespace collision New python bindings
after positional args sorting. Sorted positional args to maintain
consistent order. Add jsonschema to install requirements. Add Jinja2 to
setup.py requirements. Generate fully functional python bindings with
docs attached. Remove .travis.yml changes b/c they landed on a pr that's
already been merged. Added region env variable to travis. Create classes
that add functions/parsers for each endpoint. (#20) Add AddedCommand
superclass for all api endpoints. (#19)

Changes for v0.7.0 (2017-08-01)
===============================

remove tuple comprehension (python3 doesn't like that) Remove cli tests.
Python bindings w/ auth and some testing Autogenerated functions fully
working. making abstractions a package. Upload/Download refactor: Moved
upload/download commands to hca/api/abstractions dir. Release file
resources after completed. Cherry-picked upload-from-s3 changes Testing
head\_files. Don't regenerate python bindings. Templatize relative
imports from autogenerated. Remove unnecessary import Relative imports
from autogenerated Include all jinja files and update tests. Populate
test bundle with real data avoid namespace collision New python bindings
after positional args sorting. Sorted positional args to maintain
consistent order. Add jsonschema to install requirements. Add Jinja2 to
setup.py requirements. Generate fully functional python bindings with
docs attached. Remove .travis.yml changes b/c they landed on a pr that's
already been merged. Added region env variable to travis. Create classes
that add functions/parsers for each endpoint. (#20) Add AddedCommand
superclass for all api endpoints. (#19)

Changes for v0.6.0 (2017-07-12)
===============================

Changes for v0.5.0 (2017-07-12)
===============================

Changes for v0.4.0 (2017-07-12)
===============================

Changes for v0.3.0 (2017-07-12)
===============================

v0.3.0 Support uploading bundle from staged s3 bucket to DSS. Fix upload
from local bug.

Changes for v0.3.0 (2017-07-12)
===============================

Support uploading bundle from staged s3 bucket to DSS. Fix bug in hca
upload.

Changes for v0.2.0 (2017-07-12)
===============================

-  Initial release.

Changes for v0.1.0 (2017-06-27)
===============================

-  Demo version pre-release

Command line interface that interacts with the Human Cell Atlas data
store REST API.

Current functionality: Retrieve or register a data file. Retrieve or
register a data bundle (collection of data files). Upload full directory
to cloud, register given files, and collect them into a bundle. Download
a bundle or file from HCA data store to local.

Changes for v1.0.0 (2017-06-26)
===============================

Changes for v0.0.8 (2017-06-06)
===============================

Test release
------------

Changes for v0.0.7 (2017-06-06)
===============================

Test release
------------

Changes for v0.0.6 (2017-06-06)
===============================

Test release
------------

Changes for v0.0.5 (2017-06-06)
===============================

Test release
------------

Changes for v0.0.4 (2017-06-06)
===============================

Test release
------------

Changes for v0.0.3 (2017-06-06)
===============================

Test Release
------------

Changes for v0.0.2 (2017-06-06)
===============================

Test release
------------

Changes for v0.0.1 (2017-06-06)
===============================

Test Release
------------

Changes for v0.0.1 (2017-06-06)
===============================

Test Release
------------

Changes for v0.0.1 (2017-06-06)
===============================

Test release
~~~~~~~~~~~~

