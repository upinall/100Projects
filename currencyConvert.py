import requests # import lib to use http calls

apilinkbase = 'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/' # real time currency API

def main():
    inputMon = input("Which currency are you converting from? ") # if you have US Dollars use "usd"
    outputMon = input("Which currency are you converting to? ") # if you want to convert to japanese yen you would input "jpy"
    amount = input("How much is the amount you are converting? ") # integer amount user wants to be converted..
    apiLinkUpdated = apilinkbase + str(inputMon) + '/' + str(outputMon) + '.json' # update url with new values "usd/jpy.json" with example from above.
    outputJSON = requests.get(apiLinkUpdated, verify=False).json() # run api
    conversionRate = outputJSON.get(str(outputMon)) # get api value
    conversionOutput = round(float(amount) * float(conversionRate), 2) # do calculation to find conversion and round to second decimal.
    print(str(conversionOutput) + " " + outputMon.upper()) # terminal output
    return str(conversionOutput) + " " + outputMon.upper() # output if used in other program.
if __name__ == '__main__': main()
