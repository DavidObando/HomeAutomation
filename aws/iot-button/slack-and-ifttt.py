import ssl, socket, urllib, sys

def lambda_handler(event, context):
	port = 6667
	slackhost = "<Slack Host Server IRC URL>"
	channel = "<Slack Channel (ex #general) or User account to send to (ex. slackbot)>"
	user = "<Your Slack User>"
	password = "<Slack IRC Gateway Password>"
	irc = ssl.wrap_socket(socket.socket())
	irc.connect((slackhost, port))
	irc.send("NICK "+ user +"\r\n")
	irc.send("USER {0} 0 * :{0}\r\n".format(user))
	irc.send("PASS " + password + "\r\n")

	while True:
		msg = irc.recv()
		sys.stdout.write(msg)
		sys.stdout.flush()
		if ":End of MOTD command" in msg:
			break

	irc.send("PRIVMSG "+ channel + " :Starting IFTTT Maker channel routine.\r\n")
	irc.send("QUIT \r\n")
	irc.close()
  
 
	iftttmakerkey = "<Key from IFTTT Maker channel>"
	ifttturl = "https://maker.ifttt.com/trigger/IoT-button-SINGLE/with/key/"+ iftttmakerkey
	urllib.urlopen(ifttturl)
