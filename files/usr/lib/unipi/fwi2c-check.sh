#!/bin/sh

UNIPI_PRODUCT_ID="$(cat /run/unipi-plc/unipi-id/platform_id)"
LEDFILE="/usr/share/unipi-os-configurator/ledmaps/${UNIPI_PRODUCT_ID:-.unknown.}"

if ! test "$LEDFILE"; then
  # it is OK to finish with board without ledproxy
  echo 'WARNING led proxy map not defined for this product.'
  exit 0
fi

if fwi2c | grep -q 'Bootloader only mode'; then
    echo 'ERROR fwi2c in bootloader mode'
    exit 1
fi
if ! /usr/bin/fwi2c --read-conf=/tmp/0000 >/dev/null 2>&1; then
    echo 'ERROR fwi2c --read-conf'
    exit 1
fi
if ! diff /tmp/0000 "$LEDFILE"  >/dev/null; then
    rm -f /tmp/0000
    echo 'ERROR fwi2c conf incorrect'
    exit 1
fi
echo "true"
rm -f /tmp/0000
exit 0
