#!/usr/bin/python
# custom_service.py

def inventory_custom_service(info):
    return [(None, None)]

def check_custom_service(_no_item, _no_params, info):
    service_status = info[0][0]
    if service_status == "ok":
        return (0, "OK - Service is running")
    elif service_status == "warning":
        return (1, "WARNING - Service is in warning state")
    elif service_status == "critical":
        return (2, "CRITICAL - Service is in critical state")
    else:
        return (3, "UNKNOWN - Service state unknown")

check_info["custom_service"] = {
    'check_function': check_custom_service,
    'inventory_function': inventory_custom_service,
    'service_description': 'Custom Service',
    'has_perfdata': False,
}
