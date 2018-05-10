#!/usr/bin/python

accounts = open('accs.txt','r')
proxies = open('proxies.txt','r')

if (accounts.mode == 'r') & (proxies.mode == 'r'):
    i = 1
    for i in range(1):
        r_host_port = proxies.readline()
        print (r_host_port)
        r_user_name = accounts.readline()
        print (r_user_name)
        r_password = accounts.readline()
        print (r_password)
        DATABASE = dict(
            textSearch = "I want this shirt",
            enable_change_proxy=False,
            host_port = r_host_port,
            user_name = r_user_name,
            password = r_password
        )
        #print (DATABASE['port'])