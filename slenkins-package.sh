#!/bin/sh -e
current_dir=$(pwd)
destination_repository='/home/asmorodskyi/source/hpc_package'
cd "$destination_repository"
if [ $# -eq 0 ]; then
osc -A ibs build SLE_12_SP1 --no-verify --no-init; osc -A ibs build SLE_12_SP2 --no-verify --no-init
slenkins-vms.sh -i client=SLE_12_SP2_openQA-x86_64-minimal_with_sdk_installed -i server=SLE_12_SP2_openQA-x86_64-minimal_with_sdk_installed -l tests-hpc
else
slenkins-vms.sh -i client=SLE_12_SP2_openQA-x86_64-minimal_with_sdk_installed -i server=SLE_12_SP2_openQA-x86_64-minimal_with_sdk_installed tests-hpc
fi
cd $current_dir