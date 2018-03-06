import subprocess
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--host')
parser.add_argument('--distri')
parser.add_argument('--version')
parser.add_argument('--flavor')
parser.add_argument('--arch')
parser.add_argument('--iso')
parser.add_argument('--build')
parser.add_argument('--test')
args = parser.parse_args()
allargs = '/usr/bin/openqa-client isos post _NOOBSOLETEBUILD=1 DESKTOP=textmode '
if args.host:
    allargs += '--host ' + args.host
else:
    allargs += '--host https://openqa.suse.de'
if args.distri:
    distri = args.distri
else:
    distri = 'SLE'
if args.version:
    version = args.version
else:
    version = '15'
if args.flavor:
    flavor = args.flavor
else:
    flavor = 'Installer-DVD'
if args.arch:
    arch = args.arch
else:
    arch = 'x86_64'
if args.build:
    build = args.build
else:
    build = '489.1'

if args.test:
    allargs += ' TEST=' + args.test


allargs += ' BUILD={0} DISTRI={1} VERSION={2} FLAVOR={3} ARCH={4} ISO={1}-{2}-{3}-{4}-Build{0}-Media1.iso'.format(
    build, distri, version, flavor, arch)


print 'Command to execute: \n' + allargs
subprocess.call(allargs, shell=True)
