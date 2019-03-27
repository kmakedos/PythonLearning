import time
win_hosts_path = "C:\Windows\System32\drivers\etc\hosts"
unix_hosts_path = "/etc/hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com"]

f = open(unix_hosts_path, 'a+')

for website in website_list:
    f.write(redirect + " " + website + '\n')
f.close()
time.sleep(10)

f = open(unix_hosts_path, 'r+')
content = f.readlines()
f.seek(0)
for line in content:
    if not any(website in line for website in website_list):
        f.write(line)
f.truncate()
