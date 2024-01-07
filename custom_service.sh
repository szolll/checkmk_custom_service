#!/bin/bash
# custom_service.sh

# Replace this with the actual check logic for your service
service_status="ok" # Possible values: ok, warning, critical, unknown

case "$service_status" in
    ok)
        echo "0 Custom_Service - OK Service is running"
        ;;
    warning)
        echo "1 Custom_Service - WARNING Service is in warning state"
        ;;
    critical)
        echo "2 Custom_Service - CRITICAL Service is in critical state"
        ;;
    *)
        echo "3 Custom_Service - UNKNOWN Service state unknown"
        ;;
esac
