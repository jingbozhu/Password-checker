import requests 
import hashlib
import inspect 
import sys

# test hash :744c76fb28dd5e7b83a1a1a4d09e9cbb049ae667



 
def request_api_data(char):
	url = "https://api.pwnedpasswords.com/range/" + char
	result = requests.get(url)
	if result.status_code != 200 :
		raise RuntimeError(f'Error fetching: {result.status_code},check api and try again')
	return result.text

def check_password(password):
	sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest()
	# print(sha1password)
	head , tail = sha1password[:5] , sha1password[5:]

	response = request_api_data(head)
	return result(tail,response)


def result(hash_to_check, hashes):
	hashtable = (line.split(":")for line in hashes.splitlines())
	for h, count in hashtable:
		if h.lower() == hash_to_check:
			return count
	return 0
	 

def main(args):
	for password in args:
		count = check_password(password)
		if count:
			print(f"{password} is breached {count} times!")
		else:
			print(f"Your password {password} is safe")
	return print("done")

main(sys.argv[1:])
