# Rodrigo Alcover
# 26/10/2021
# CIS-216-12292 
# Python Programming

import hashlib
import string

def crack_password(hash):
    secret_password = 'duck' # Password to guess
    hash = hashlib.md5(secret_password.encode()).hexdigest()#Encode the password to hash
    print("The hash of {!r} is: {}".format(secret_password, hash))
    del secret_password # Delete the secret password 

    variations = string.ascii_lowercase # Will check all ascii in order
    total_tries = 0 # set the total tries to 0
    for first_letter in variations:#try first letter
        for second_letter in variations:#try second second letter
            for third_letter in variations:#try second letter
                for third_letter in variations:#try third third letter
                    for four_letter in variations:#try four four letter
                        password_guess = first_letter + second_letter + third_letter + four_letter #align all letters
                        hash_guess = hashlib.md5(password_guess.encode()).hexdigest()#encode the password guessed
                        total_tries += 1 # add 1 to the total tries
                        print("Guessing: {} - {}".format(password_guess, hash_guess))#Print the progress
                        if hash_guess == hash:#Compare the hash guess with the pasword hash 
                            print("The password must be '{}', we found it after {} tries!".format(
                            password_guess, total_tries))#Print the results
                            return 
    print("Password not found!")#Print this if the password is not found
    
  
#call the function
crack_password(hash) 


# 12 hs is the total development time for this assignmet.

# I run into trouble importing functions. I Got more and worst issues with compatibility, 
# and problems importing modules for other assignments. Like Web scrapper. 
# Steven H Johnson told me "Python works on a Mac, but has quirks." 

   


