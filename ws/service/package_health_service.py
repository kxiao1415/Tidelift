from datetime import datetime
import os
import csv
import config


def get_license_by_name(package_name):
    licenses_file = os.path.join(config.basedir, 'ws/data/licenses.csv')

    file = open(licenses_file)
    reader = csv.reader(file, delimiter=',')
    for name, license in reader:
        if package_name == name:
            return license

    return None


def get_vulnerabilities_by_name_and_version(package_name, version):
    vulnerabilities = []

    vulnerabilities_file = os.path.join(config.basedir, 'ws/data/vulnerabilities.csv')
    file = open(vulnerabilities_file)
    reader = csv.reader(file, delimiter=',')
    for id, name,ver, desc, created in reader:
        if name == package_name and version == ver:
            vulnerability = {}
            vulnerability['id'] = id
            vulnerability['description'] = desc
            vulnerability['created'] = datetime.fromtimestamp(int(created)).strftime("%Y-%m-%dT%H:%M:%SZ")
            vulnerabilities.append(vulnerability)
            return vulnerabilities

    return None
