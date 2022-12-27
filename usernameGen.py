import random, requests

database = 'https://www.mit.edu/~ecprice/wordlist.10000' # shoutout MIT.

def main():
    response = requests.get(database, verify=False) # get list of words from http database
    words = response.content.decode() # decode/get content
    wordsList = words.splitlines() # split each line into a list.
    twoWords = random.choice(wordsList).capitalize() + ' ' + random.choice(wordsList).capitalize()
    print(twoWords) # print output!
    return twoWords # in case needs to be used in other program.

if __name__ == '__main__': main()

'''
Username Generator! written by upinall

This script will give a random set, of 2, words to the user based on an online database offered by MIT.

Special Note: I work on these scripts within a VPN environment so I get SSL errors! If you use this code... PLEASE EDIT THE RESPONSE VAR TO VERIFY=TRUE. Thanks!

'''