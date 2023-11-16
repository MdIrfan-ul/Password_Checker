import requests
import hashlib
import sys

def api_data(query_char):
  url = 'https://api.pwnedpasswords.com/range/' + query_char
  res = requests.get(url)
  if res.status_code!= 200:
    raise RuntimeError(f'Error Fetching:{res.status_code}, check the api and try again')
  return res

def get_leaked_pass_count(hashes, hashes_for_the_checking):
  hashes = (lines.split(':') for lines in hashes.text.splitlines())
  for hash, check in hashes:
    if hash == hashes_for_the_checking:
      return check
  return 0    

def pwned_passwords(password):
  sha1pass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
  first5, last = sha1pass[:5], sha1pass[5:]
  response = api_data(first5 )
  return get_leaked_pass_count(response, last)

def main(args):
  for password in args:
    check = pwned_passwords(password)
    if check:
     print(f'{password} was found {check} You Should Probably change it!!!')
    else:
     print(f'{password} NOT FOUND Carry On!')    
  return 'done!'

if __name__ == '__main__':
  with open('InputPassword.txt', 'r') as file:
    lines = file.readlines()
    main(lines)   
  main(sys.argv[1:])

