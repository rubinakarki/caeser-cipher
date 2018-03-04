import os 
import string 
def renameFiles():
	file = os.listdir(r"C:\prank")#list the item in the directory in the given path
	#print (file)
	rr= os.getcwd()#current working directory
	print("current working directory is :"+ rr) 
	os.chdir(r"C:\prank")#change the directory path

	for f in file:
		translation_table= str.maketrans(" "," ","0123456789")#table consists of mapping of first 
																#and second string or anything such as ("abc","ghi","bc=delete character")
															  #a-g,b-h,c-i,,,,,,string=abcdef------>ghi]def
		os.rename(f,f.translate(translation_table))			
	os.chdir(rr) 
	
renameFiles()