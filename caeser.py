print("enter the sentence to be encrypted ")
plainText  = input()
shiftKey = 3


#for encryption
def check(alphabet):

	if(alphabet >= 97  and  alphabet <= 122):
		newWord = chr(alphabet)
		print(newWord, end ="")
	else:
		letterExcept = alphabet - 26
		print(chr(letterExcept),end ="")

		

for letter in plainText:
	each = letter.lower()
	cipher =  (ord(each) + shiftKey) 
	check(cipher)






	

	







	


	
