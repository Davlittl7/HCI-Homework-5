def encryption(text,s):
   encryptedText = ""
   
   # goes through the plaintext in the for loop
   for i in range(len(text)):
      char = text[i]
      
      # First, looks to encrypt any uppercase characters in the plaintext
      if (char.isupper()):
         encryptedText += chr((ord(char) + s-65) % 26 + 65)
      # Then, the program looks for any spaces within the text argument
      elif (char == " "):
         encryptedText += " "
      # Finally, it looks to encrypt lowercase characters in plaintext
      else:
         encryptedText += chr((ord(char) + s - 97) % 26 + 97)
   return encryptedText

text = "Davonte Littleton"
shift = 20

print ("Plain Text: " + text)
print ("Shift: " + str(shift))
print ("Encrypted Text: " + encryption(text,shift))
