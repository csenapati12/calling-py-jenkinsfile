def main():
	target_machine_ip = sys.argv[1]
 // a = int(sys.argv[1])
	uri = "https://" + target_machine_ip + ":30443/auth/realms/hiota/protocol/openid-connect/token"
	print(uri)
	
main()
