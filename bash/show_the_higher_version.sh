#!/usr/bin/env bash


# Define URL
var1='https://releases.hashicorp.com/vault/index.json'

# Export the higher version of product
curl -sL $var1 | jq -r '.versions | to_entries[] | .value.version' | sort --version-sort | grep -v 'beta' | tail -1
