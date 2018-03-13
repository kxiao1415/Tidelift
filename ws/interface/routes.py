from ws import latest
import json
from urllib2 import Request, urlopen

from ws.service import package_health_service


@latest.route('/package/health/<package_name>/<version>', methods=['GET'])
def get_package_health(package_name, version):
    """
    Get package health by package name and version

    **sample request**

        curl -X GET 'http://localhost:5000/package/health/dummy/0.9'

    **sample response**

        {
            "name": "dummy",
            "version": "0.9",
            "license": "MIT",
            "vulnerabilities": [
                {
                    "id": "v2017-001",
                    "description": "this is a dummy cve",
                    "created": "2017-09-01T14:32:93Z"
                }
            ]
        }

    """

    result = {}

    license = package_health_service.get_license_by_name(package_name)
    vulnerabilities = package_health_service.get_vulnerabilities_by_name_and_version(package_name, version)

    result['name'] = package_name
    result['version'] = version

    if license:
        result['license'] = license

    if vulnerabilities:
        result['vulnerabilities'] = vulnerabilities

    return json.dumps(result)


@latest.route('/package/releases/<package_name>', methods=['GET'])
def get_package_releases(package_name):
    """
    Get package releases by package name

    **sample request**

        curl -X GET 'http://localhost:5000/package/releases/tiny-tarball'

    **sample response**

        {
            "name": "tiny-tarball",
            "latest": "1.0.0",
            "releases": [
                "1.0.0"
            ]
        }

    """

    result = {}

    url = 'https://registry.npmjs.org/{0}'.format(package_name)

    try:
        request = Request(url)
        response = urlopen(request)
    except:
        return 'package not found'

    json_response = json.loads(response.read())

    result['name'] = json_response['name']
    result['latest'] = json_response['dist-tags']['latest']

    result['releases'] = []
    for release in json_response['versions']:
        result['releases'].append(release)

    return json.dumps(result)
