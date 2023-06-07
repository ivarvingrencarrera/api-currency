#!/usr/bin/env bash

GIT_PRE_PUSH='#!/bin/bash
cd $(git rev-parse --show-toplevel)
poetry run make linting && poetry run make testing
'

echo "$GIT_PRE_PUSH" > .git/hooks/pre-push
chmod +x .git/hooks/pre-*