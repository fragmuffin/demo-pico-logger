#!/usr/bin/env bash
cd $(dirname $0)
source=src

pushd $source
mpremote fs --recursive cp ./* :
popd
