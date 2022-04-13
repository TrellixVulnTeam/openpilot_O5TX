#!/usr/bin/bash

export OMP_NUM_THREADS=1
export MKL_NUM_THREADS=1
export NUMEXPR_NUM_THREADS=1
export OPENBLAS_NUM_THREADS=1
export VECLIB_MAXIMUM_THREADS=1
export FINGERPRINT="LANDROVER RangeRover Vogue 2017"

if [ -z "$REQUIRED_NEOS_VERSION" ]; then
  export REQUIRED_NEOS_VERSION="19.1"
fi

if [ -z "$AGNOS_VERSION" ]; then
  export AGNOS_VERSION="4"
fi

if [ -z "$PASSIVE" ]; then
  export PASSIVE="0"
fi

export STAGING_ROOT="/data/safe_staging"
