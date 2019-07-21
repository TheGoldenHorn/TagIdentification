######################
#SCRIPT TO LOAD LINKS#
#  By Ayush          # 
######################           
import webdriver
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
     
    return i + 1


filename = raw_input('Enter the filename.txt containing links: ')
#filename="urls.txt"
max_count=file_len(filename)
file=open(filename,"w+")
print "total links are" 
print str(max_count) + "\n"
num=max_count

for i in range (0, max_count) :
	try:
		link=file.readline()
		print("Please wait, loading...")
		print num
		print link
		num-=1

		print("\n Do not press ENTER before 'LOADED' ")

		browser.get(link)
		#time.sleep(10)
		#wait_for_tag()
		print("LOADED \n")

		
		print("Press ENTER for the next link")
		pause=raw_input(" ")
		
		
	except Exception as e:
		print e
		print("raised")
		pass

file.close()