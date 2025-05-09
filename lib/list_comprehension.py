#!/usr/bin/env python3

#pseudocode
#define a function called return_evens 
# and takes num_list as parameter
#loop through the num_list 
#check if the number is even 
#return all the even number 

def return_evens(num_list):
    return [number  for number in num_list if number % 2 == 0 ]
    
print(return_evens([0, 1, 3, 5, 7, 8, 9]))


#Pseudocode
#define a function named make_exclamation
#the function takes list of sentence strings as parameter
#loop through the list of sentence 
#add an exclamantion mark to the end of each sentence

def make_exclamation(sentence_list):
    # for word in sentence_list:

    #     new_word = word + "!"
    #     print(new_word)
    return [ word + "!" for word in sentence_list ]
 
print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))