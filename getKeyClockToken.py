import sys
def main():
	target_machine_ip = sys.argv[1]
 	uri = "https://" + target_machine_ip + ":30443/auth/realms/protocol/openid-connect/token"
	print(uri)	
main()
