# =============================================================================
# Created By  : Raul Sainz
# Created Date: 2021-03-21
# =============================================================================
"""The Module Has Been Build for DAP Project"""
# =============================================================================
# Imports
# =============================================================================
from termcolor import colored   #Function to print console message with colors
import datetime                 #Library for getting tim
import requests                 #Library allows to send send HTTP requests
from urllib import parse        #Library to make URL request to Wikipedia API
from googletrans import Translator, constants
import warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning) #Disable warnings for SSL Certificate in WHO API
from  mypackage.classes import customError
# =============================================================================
# Function logMessage
# Gets and prints a message with a color depending on the level
# @msg str: Message to be printed
# @level int: Type of message 
#                            0 - default
#                            1 - OK (green output)
#                            2 - Error (red )
#                            2 - Warning (red )
#                            2 - Notice (red )                           
# @returns: Print console message
# =============================================================================


def logMessage(msg = 'Empty msg',level = 0,addTime = True): 
    if addTime:
        date = '[' + datetime.datetime.now().strftime("%m/%d/%Y-%H:%M:%S") + ']'
        date = colored(str(date)+': ', 'white', attrs=['reverse', 'blink'])
    else:
        date='[-]'
    if level == 0: # Default informative output
        print(date+msg)
    if level == 1: # OK output
        print(date+colored('OK: '+ msg, 'green', attrs=['reverse', 'blink']))
    if level == 2: # Error output
        print(date+colored('ERROR: '+ msg, 'red', attrs=['reverse', 'blink']))
    if level == 3: # Warning output
        print(date+colored('WARNING: '+ msg, 'yellow', attrs=['reverse', 'blink']))
    if level == 4: # Important output
        print(date+colored('NOTICE: '+ msg, 'blue', attrs=['reverse', 'blink']))
# =============================================================================
# Function confirmAction
# Ask for confirmation on a given question
# @msg str: Question to be asked for confirmation
# @returns: True if y, False everything else
# =============================================================================

def confirmAction(msg):
    reply = str(input(msg+' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        logMessage('Action confirmed',1)
        return False
    else:
        logMessage('Action rejected',3)
        return True

# =============================================================================
# Function translate_english
# Translate a text into english using googletrans library
# @text str: text to be procesed
# @returns: str processed string
# =============================================================================
def translate_english(text):
    #functions.logMessage("Traduciendo {} ...".format(text))
    translator = Translator()
    translation = translator.translate(text,src="es")
    return translation.text

# =============================================================================
# Function getWikipediaInfo
# search for wikipedia pages based on a text
# @text str: text to be searches in Wikipedia
# @numChars int: Number of chrachters to be returned from wikipedia
# @returns: 
# =============================================================================

def getWikipediaInfo(text,numChars=500):
    char_limit = 30 #number of characters to print on log messages
    hits_treashhold = 10 #min num of wikipedia hits to look for suggstion
    try:
        if text =='' or text =='NO DATA':
            return 'NO DATA'
        myRequest = requests.Session()
        URL = "https://en.wikipedia.org/w/api.php" #Wikipedia API URL
        #first query looks for the sentence
        params_q1 = { #parameters of the first query
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": text, #encode text for url
        "srqiprofile":'classic'
        }
        #logMessage('fetching wikipedia results for... "{}"'.format(text[:char_limit]))
        #first search for wikipedia titles
        query1 = myRequest.get(url=URL, params=params_q1)
        if query1.status_code != requests.codes.ok:
            raise customError("Unable to connect to Wikipedia API: {}".format(query1.status_code))
        json1 = query1.json()
        totalhits = int(json1['query']['searchinfo']['totalhits'])
        if('suggestion' in json1['query']['searchinfo']) & (totalhits<hits_treashhold):  #the query hits bellow treashold and suggestion provided         
            title = json1['query']['searchinfo']['suggestion']
            logMessage('not found "{}", suggested "{}" '.format(text[:char_limit],title[:char_limit]),3)
        else: #found a wikipedia page
            logMessage('found {} hits for "{}"'.format(json1['query']['searchinfo']['totalhits'],text[:char_limit]),1)
            title = json1['query']['search'][0]['title'] #get the first result
        #title of wikipedia page found, look for extract of the title page
        
        params_q2 = {
            "action": "query",
            "format": "json",
            "prop": "extracts",
            "titles": title,
            "exchars":numChars,
            "explaintext":1
        }
        query2 = myRequest.get(url=URL, params=params_q2)
        json2 = query2.json()
        first_key = list(json2['query']['pages'].keys())[0] #gets first key of results 
        if 'extract' in json2['query']['pages'][first_key]: #Checks if result is available
            return json2['query']['pages'][first_key]['extract'] #returns 'Extract' of wikipedia page
        else:
            logMessage('tile not found: "{}"'.format(title[:char_limit]),3)
            return 'NO DATA'        
    except Exception as e:
        logMessage(str(e),2)
        return 'NO DATA'

# =============================================================================
# Function getWHOInfo
# Gets IDC code description from the WHO API
# @idc str: text to be searches in Wikipedia
# @description str: IDC10 dode description
# @returns: 
# =============================================================================

def getWHOInfo(idc10_code):
    try:
        
       # Get TOKEN
        token = getWHO_TOKEN()
        # URL of ICD API
        uri = 'https://id.who.int/icd/release/10/'+idc10_code

        # HTTP header fields to set
        headers = {'Authorization':  'Bearer '+ token, #Send AUTH token
                    'Accept': 'application/json', #format of the result
                    'Accept-Language': 'en', #langiage of the result
                    'API-Version': 'v2'} #Version of the API            
        # make request           
        query1 = requests.get(uri, headers=headers, verify=False)
        if query1.status_code == requests.codes.unauthorized:
            logMessage('Token expired.',3)
            global WHO_API_TOKEN
            WHO_API_TOKEN = ''
            return getWHOInfo(idc10_code)
        if query1.status_code != requests.codes.ok:
            raise customError("Unable to connect to WHO API: {}".format(query1.status_code))    
        json1 = query1.json()
        if('title' in json1):  #the query contains a valid title         
            title = json1['title']['@value']
            logMessage('title found for "{}"'.format(idc10_code),1)
        else: #found a wikipedia page
            logMessage('No description found for {}'.format(idc10_code),3)
            title = 'NO DATA'
        #title of wikipedia page found, look for extract of the title page
        return title.lower()
    except Exception as e:
        logMessage('getWHOInfo: '+str(e),2)
        return 'NO DATA'
# =============================================================================
# Function getWHO_TOKEN
# Gets IDC code description from the WHO API
# @idc str: text to be searches in Wikipedia
# @description str: IDC10 dode description
# @returns: 
# =============================================================================
WHO_API_TOKEN = '' #Define global variable to store TOKEN after initially created

def getWHO_TOKEN():
    global WHO_API_TOKEN
    if WHO_API_TOKEN != '': #Checks if token already exist
        return WHO_API_TOKEN
    token_endpoint = 'https://icdaccessmanagement.who.int/connect/token'
    client_id = '04d19cc4-f7fe-4efa-a2a4-114407a4590e_1d81f3ed-6d16-4164-8aaa-cf53d3f3674f'
    client_secret = 'UZqwmhaa94sTJ0Qc00AwRSgznNUA8TbaI0c5jbK7m5A='
    scope = 'icdapi_access'
    grant_type = 'client_credentials'
    # set data to post
    payload = {'client_id': client_id, 
	   	   'client_secret': client_secret, 
           'scope': scope, 
           'grant_type': grant_type}
    try:
        logMessage('Creating API authentication TOKEN ...',4)
        # make token request
        request1 = requests.post(token_endpoint, data=payload, verify=False)
        if request1.status_code != requests.codes.ok:
            raise customError("Unable to obtain token from WHO API: {}".format(request1.status_code))
        token = request1.json()['access_token'] #Token obtained
        WHO_API_TOKEN = token #stores token in global variable 
        return WHO_API_TOKEN  #returns token value
    except Exception as e:
        logMessage(str(e),2)
        return 'NO Token received'
# =============================================================================
# Function getCauseDeathCategory
# Search for words in a given category array
# @row str: Pandas dataframe row
# @category str: name of the category
# @find_words array: list of words to search
# @returns pd.Series: 
# =============================================================================

def getDeathCategories(row,category,find_words):        
        if any(x in row['cause_death'] for x in find_words): 
            return True #if word is found, stops the search and returns True
        elif  row[category]==False: #if no matching word on 'cause_death', will look for matching words on wikipedia info 
            set1 = set(row['wiki_tokens']) 
            set2 = set(find_words) 
            if set1.intersection(set2): 
                return True 
            else: 
                return False
        else:
            return False #Not found any matching words on both columns

def getWHODeathCategory(row,category,find_words):        
        if any(x in row['icd10_desc'] for x in find_words): 
            return True #if word is found, stops the search and returns True
        elif any(x in row['wiki'] for x in find_words) and row[category]==False: #if no matching word on 'cause_death', will look for matching words on wikipedia info 
            return True
        else:
            return False #Not found any matching words on both columns

# =============================================================================
# Function getDiseaseNewsCountPerCountry
# Search newss related to a given disease
# @row str: Pandas dataframe row
# @category str: name of the category
# @find_words array: list of words to search
# @returns pd.Series: 
# =============================================================================

def getDiseaseNewsCountPerCountry(query):
    API_KEY = '9602c65fc27944c99e09b80c04ef96c8'
    myRequest = requests.Session()
    char_limit = 30
    URL = "https://newsapi.org/v2/everything" #News API URL
    try:
        
        #first query looks for the sentence
        params_q1 = { #parameters of the first query
        "apiKey": API_KEY,
        "q": query
        }
        logMessage('fetching news results for... "{}"'.format(query[:char_limit]))
        #first search for wikipedia titles
        query1 = myRequest.get(url=URL, params=params_q1)
        if query1.status_code != requests.codes.ok:
            raise mypackage.customError("Unable to connect to News API: {}".format(query1.status_code))
        json1 = query1.json()
        if json1['status'] =='ok':
            return int(json1['totalResults'])
        else:
            return 0
    except Exception as e:
        logMessage(str(e),2)
        return 'NO DATA'

