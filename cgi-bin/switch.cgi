#!/bin/sh
echo "Content-Type: text/json"
echo "Cache-Control: no-cache, must-revalidate"
echo "Expires: Sat, 26 Jul 1997 05:00:00 GMT"
# Add this header if you want to use this wit XHR calls from elsewhere.
# echo "Access-Control-Allow-Origin: *"
echo

RELAY_CTRL=/sys/class/leds/tp-link:blue:relay/brightness

case "$QUERY_STRING" in
 on)
  echo 1 > $RELAY_CTRL
  echo "{ \"on\": true }"
 ;;
 off)
  echo 0 > $RELAY_CTRL
  echo "{ \"on\": false }"
 ;;
 *)
  case "`cat $RELAY_CTRL`" in
   0) echo "{ \"on\": false }"
   ;;
   1) echo "{ \"on\": true }"
   ;;
  esac
esac
