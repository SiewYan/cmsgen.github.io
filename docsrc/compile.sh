#!/bin/bash

make html
sphinx-build -b rinoh source _build/rinoh
