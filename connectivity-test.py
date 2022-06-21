import yaml, socket

def get_endpoints(endpoints_yaml):
  with open(endpoints_yaml, 'r') as endpointsfile:
    endpoints = yaml.safe_load(endpointsfile)
  return endpoints['endpoints']

def connection_validate(endpoints_dict):
  status = {}
  success_list = []
  failed_list = []
  for endpoint in endpoints_dict:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3) 
    result = sock.connect_ex((endpoint['host'],endpoint['port']))
    if result == 0:
      print("Connection to host {0} on port {1} is successfull".format(endpoint['host'], endpoint['port']))
      success_list.append(endpoint)
    else:
      print("Connection to host {0} on port {1} FAILED".format(endpoint['host'], endpoint['port']))
      failed_list.append(endpoint)
    sock.close()
  status["success"] = success_list
  status["failed"] = failed_list
  return status

if __name__ == "__main__":
  endpoints = get_endpoints("endpoints.yaml")
  result = connection_validate(endpoints)
  if len(result['failed']) > 0:
    print("Some host connectivity test failed")
    exit(1)
  else:
    print("Connectivity test for all hosts passed")
