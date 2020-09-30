def webpage():
	import webbrowser
	web1 = "http://www.bbc.co.uk/"
	web2 = "http://en.wikipedia.org/wiki/Main_Page"
	web3 = "http://www.nasa.gov/"
        web4 = "http://www.netflix.com/"
        web5 = "http://www.motorsport.com/"

	answer = int(input("""
	1 To open BBC
	2 To open Wikipedia
	3 To open NASA
        4 To open Netflix
        5 To open Motorsport.com
	"""))

	if answer == 1:
		webbrowser.open(web1)
	elif answer == 2:
		webbrowser.open(web2)
	elif answer == 3:
		webbrowser.open(web3)
        elif answer == 4:
		webbrowser.open(web4)
	elif answer == 5:
		webbrowser.open(web5)

#main program
webpage()
