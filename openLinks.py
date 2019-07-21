import webbrowser

#includde a file
filename = raw_input('Enter the filename.txt containing links: ')
with open(filename, 'rU') as in_file:
    urls = in_file.read().split('\n')
#urls = ['https://www.tampatriallawyers.com/','http://www.parcprovence.com','http://EnglishGardentone.net','http://www.ver-sys.com','http://www.tampatriallawyers.com','http://www.riamobilesolutions.com','http://www.apogeeelitesales.com','http://www.vsamarketing.com','http://www.aquaabode.com','http://www.anchorsaweighenergy.com','http://www.dalkepm.com','http://www.janscientific.com/','http://www.bndcommercial.com','http://www.generalbiofuels.com','http://www.architexturaldesigns.com','http://www.tudalwinery.com','http://www.Chesapeake-Care.org','http://www.identitymate.com','http://www.retinaboston.com','http://www.northridgevillasapts.com/','https://hightechorlando.com']
    #urls = urls[:]
num = 0
for url in urls:
	if(num==0):
		webbrowser.open_new(url)
	else:
		webbrowser.open_new_tab(url)
	
	num += 1
	if (num%5==0):
		raw_input()
		pass

print "Tags completed."
print " .......Press a key to exit......."		