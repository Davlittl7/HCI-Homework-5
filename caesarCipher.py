def encrypt(text,s):
   result = ""
   # transverse the plain text
   for i in range(len(text)):
      char = text[i]
      # Encrypt uppercase characters in plain text
      
      if (char.isupper()):
         result += chr((ord(char) + s-65) % 26 + 65)
      # Encrypt lowercase characters in plain text
      elif (char == " "):
         result += " "
      else:
         result += chr((ord(char) + s - 97) % 26 + 97)
   return result
#check the above function
text = "Davonte Littleton"
s = 20

print ("Plain Text : " + text)
print ("Cipher: " + encrypt(text,s))
