# =============================================================================
# Created By  : Raul Sainz
# Created Date: 2021-03-21
# =============================================================================
"""The Module Has Been Build for DAP Project"""
# =============================================================================
# Imports
# =============================================================================
import datetime                 #Ligrary for getting tim
import pandas as pd

import pymongo                  #MongoDB Driver
import pymongo.errors 
import urllib                   #Library to url encode the password
import os                       #os library to interact with host OS
import math
from  mypackage import functions
from  mypackage.classes import customError
pd.set_option('MAX_COLUMNS', None) #Set pandas to display all the columns in dataset


# =============================================================================
# Function getMongoClient
# Provides driver for MongoDB connection
# @db str: Name of the Database to connect
# @returns: pymongo.mongo_client.MongoClient
# =============================================================================
#Function to connect to Mongo DB
def getMongoClient(db='TestDB'):  
    try:
        usr = 'x19158696'
        pwd = urllib.parse.quote('3Opg064UlD@XJ@vkaZ')
        #pwd ='dasdadas'
        cluster = 'ClusterDAP'
        url = "mongodb+srv://{0}:{1}@{2}.ozzj2.mongodb.net/{3}?retryWrites=true&w=majority"
        client = pymongo.MongoClient(url.format(usr,pwd,cluster,db))
        #test = client.db
        return client
    #except (AttributeError, pymongo.errors.ConfigurationError):
    except Exception as e:
        functions.logMessage(str(e),2)
        return False
# =============================================================================
# Function getMongoCollection
# Provides driver for MongoDB connection and collection object
# @db str: Name of the Database to connect
# @collection str: Name of the Database to connect
# @returns: pymongo.mongo_client.MongoClient
# =============================================================================
#Function to connect to Mongo DB
def getMongoCollection(dbname,collname):  
    try:        
        client = getMongoClient(db=dbname)
        db_obj = client[dbname]
        collection = db_obj[collname]
        return collection
    except Exception as e:
        functions.logMessage(str(e),2)
        return False
# =============================================================================
# Function getMongoClient
# Provides Checks status of MongoDB connection
# @client str: ymongo.mongo_client.MongoClient
# @returns: True|False
# =============================================================================
def testMongoClient(client):
    try:
        print(client.server_info()) # force connection on a request as the
                         # connect=True parameter of MongoClient seems
                         # to be useless here 
    except pymongo.errors.ServerSelectionTimeoutError as err:
        # do whatever you need
        print(err)



# =============================================================================
# Function uploadCSV
# Imports data from CSV file imports it into pandas data frame and saves records into a given MongoDB 
# @fileName str: Name of CSV File
# @dbname str: Name of the MongoDB database
# @collection str: name of the collection
# @samplesize float: percentage of the origiginal data set to sample and upload
# @maxWriteBatchSize = number or fows to save at each batch
# @output: console messages
# =============================================================================
def uploadCSV(fileName, dbname, collection, samplesize=1 , batchSize = 50000):
    maxWriteBatchSize = 100000 #maxWriteBatchSize value of 100,000 for MongoDB insert_many()
    try:
        if not all([fileName, dbname, collection]): #Checks if any of the parmeters is empty
            raise customError("Empty function parameters")
        if batchSize > maxWriteBatchSize:
            raise customError("Batch {} Size too large".format(batchSize))
        if not os.path.exists(fileName):
            raise customError("File not found, please check") 
        functions.logMessage("Loading file '{}' into memory...".format(fileName))
        data = pd.read_csv(fileName) 
        numRows = data.shape[0]
        functions.logMessage("File {} succesfuly loaded: {} registries".format(fileName,numRows),1)
        functions.logMessage("Connecting to mongo DB {} ...".format(dbname))
        myMongoClient = getMongoClient(dbname)
        db = myMongoClient[dbname]
        collection = db[collection]
        data = data.sample(frac=samplesize, replace=True, random_state=42)
        numRows = data.shape[0]
        functions.logMessage("Sampling file at {:.1f}%  loaded {} registries".format(samplesize*100,numRows),1)
        if not isinstance(myMongoClient,pymongo.mongo_client.MongoClient):
            raise customError("Mongo Client not available")
        #data.reset_index(inplace=True) #Add index to records for identification
        if numRows>batchSize:
            steps = math.floor(numRows/batchSize) #number of steps to perform upload
            rest = numRows % batchSize #Remaining records
            for batch in range(steps):
                ini=batch*batchSize
                fin=ini+batchSize
                functions.logMessage('({}/{}) Inserting records {} to {}...'.format(batch+1,steps+1,ini,fin))
                data_dict = data[ini:fin].to_dict("records") #export data to dictionary
                collection.insert_many(data_dict) #Insert dictionary in mongoDB
                functions.logMessage('({}/{}) Inserted {} records.'.format(batch+1,steps+1,len(data_dict)),1)
                if(batch==steps-1): #If final batch save the remaining records
                    functions.logMessage('({}/{}) Inserting records {} to {}..'.format(batch+2,steps+1,fin,fin+rest))
                    data_dict = data[fin:fin+rest].to_dict("records") #export data to dictionary
                    collection.insert_many(data_dict) #Insert dictionary in mongoDB 
                    functions.logMessage('({}/{}) Inserted {} records.'.format(batch+2,steps+1,len(data_dict)),1)
        else:
            functions.logMessage('Inserting records...')
            data_dict = data.to_dict("records") 
            collection.insert_many(data_dict) #Insert dictionary in mongoDB
            functions.logMessage('Inserted {} records.'.format(numRows),1)
        functions.logMessage('Finshed Mongo exporation,  inserted {} records.'.format(numRows),4)
        getDBStatistics(dbname) #Prints DB statistics for reference
    except Exception as e:
        functions.logMessage(str(e),2)
        if 'myMongoClient' in locals():
            if isinstance(myMongoClient,pymongo.mongo_client.MongoClient):
                myMongoClient.close()
        if 'data' in locals():
            del data #unset dataframe
    finally:
        if 'myMongoClient' in locals():
            myMongoClient.close() #Close DB connection
            functions.logMessage('Closing DB connection...')
        if 'data' in locals():
            del data #unset dataframe
            functions.logMessage('deleting temp dataframe...')
# =============================================================================
# Function getDBStatistics
# Prints information about the current mongoDB instance
# @db str: Name of Data Base
# @output: console message
# =============================================================================
def getDBStatistics(db='TestDB'):
    try:
        myMongoClient = getMongoClient()
        db = myMongoClient[db]
        db_stats = db.command("dbstats") #Get DB Information and stats
        c_stats = db.command("collstats", "events") #Get collecction Information and stats
        database = str(db_stats['db'])
        datasize = db_stats['dataSize'] / 1024
        objects = int(db_stats['objects'])
        collections = str(db_stats['collections'])
        usage = (datasize/512000)*100
        stats = "Database:   {}  \n\t\t\t       Objects:    {:,} \n\t\t\t       Collectons: {} \n\t\t\t       Size:       {:,.2f} ({:.1f}%)".format(database,objects,collections,datasize,usage)
        functions.logMessage(stats,4)
        myMongoClient.close() #Close DB connection
    except Exception as e:
        functions.logMessage(str(e),2)
        if 'myMongoClient' in locals():
            if isinstance(myMongoClient,pymongo.mongo_client.MongoClient):
                myMongoClient.close()

# =============================================================================
# Function getCollection
# Returns pandas Dataframe with collection registries
# @db str: Name of Data Base
# @output: console message
# =============================================================================
def dropCollection(dbname,cname):
    try:
        #txt = 'Are you sure you want to delete collection {}?'.format(cname)
        #if(functions.confirmAction(msg=txt)):
         #   raise customError("Drop collection {} from db {} cancelled".format(cname,dbname))
        #if not all([dbname, cname]): #Checks if any of the parmeters is empty
        #    raise customError("Empty function parameters")
        functions.logMessage("Connecting to mongo DB {} ...".format(dbname))
        myMongoClient = getMongoClient(dbname)
        db = myMongoClient[dbname]
        collection = db[cname]
        functions.logMessage("Droping collection: {} ...".format(cname))
        response = collection.drop() #execure drop collection
        myMongoClient.close() #Close DB connection
        functions.logMessage('Finished droped {} collection.'.format(cname),1)
    except Exception as e:
        functions.logMessage(str(e),2)
        if 'myMongoClient' in locals():
            if isinstance(myMongoClient,pymongo.mongo_client.MongoClient):
                myMongoClient.close()
    finally:
        getDBStatistics(dbname) #Prints DB statistics for reference


# =============================================================================
# Function getCollection
# Returns pandas Dataframe with collection registries
# @db str: Name of Data Base
# @output: console message
# =============================================================================
def getCollectionDF(dbname,cname,dict={}):
    try:
        if not all([dbname, cname]): #Checks if any of the parmeters is empty
            raise customError("Empty function parameters")
        functions.logMessage("Connecting to mongo DB {} ...".format(dbname))
        myMongoClient = getMongoClient(dbname)
        db = myMongoClient[dbname]
        collection = db[cname]
        functions.logMessage("Query collection: {} ...".format(cname))
        results = list(collection.find())
        num = len(results)
        if num > 1:
            functions.logMessage("Fount {} files".format(num),1)
            data = pd.DataFrame(results)
            return data
        else:
            functions.logMessage("No files found on {}, returning empty data frame".format(cname),3)
            return pd.DataFrame()
    except Exception as e:
        functions.logMessage(str(e),2)
        if isinstance(myMongoClient,pymongo.mongo_client.MongoClient):
            myMongoClient.close()
    finally:
        if 'myMongoClient' in locals():
            if isinstance(myMongoClient,pymongo.mongo_client.MongoClient):
                myMongoClient.close() #Close DB connection  
                functions.logMessage('Closing DB connection...')
        if 'data' in locals():
            del data #unset dataframe
            functions.logMessage('deleting temp dataframe...')
# =============================================================================
# Function replaceColumn
# Replace Mongo Document value to another column value
# @dbname str: Name of Data Base
# @cname: name of the collection to be updated
# @replace object
#               -new: name of the new column
#               -old: name of the current column
#               -vals: dictionary with values to replace
# =============================================================================
def replaceColumn(dbname,cname,replace={}):
    try:
        if not all([dbname, cname,replace]): #Checks if any of the parmeters is empty
            raise customError("Empty function parameters")
        if 'vals' in replace:
            functions.logMessage("Performing: {} replacements".format(str(len(replace['vals']))),4)
        if (len(replace['vals'])<1): #Checks if any values on replacement dictionary
            raise customError("replace dictionary cannot be empty")   
        functions.logMessage("Connecting to mongo DB {} ...".format(dbname))
        myMongoClient = getMongoClient(dbname)
        db = myMongoClient[dbname]
        collection = db[cname]
        functions.logMessage("Updating collection: {} ...".format(cname))
        total_rows = 0
        for key,val in replace['vals'].items():#loops trough the values to be changed
            myquery = { replace['old']: key } # select query with old coluns value
            newvalues = { "$set": { replace['new']: val } } #creates new column with new value
            results = collection.update_many(myquery, newvalues)
            rows = int(results.modified_count)
            total_rows+=rows
            if rows > 0:
                functions.logMessage("column {} = {} -> {} = {} -- {}".format(replace['old'],key,replace['new'],val,results.modified_count),1 )
            else:
                functions.logMessage("No documents found for {} = {} -> {} = {}".format(replace['old'],key,replace['new'],val),4 )
        functions.logMessage('Finished replacement {} rows processed.'.format(total_rows),1)
    except Exception as e:
        functions.logMessage(str(e),2)
        if 'myMongoClient' in locals():
            if isinstance(myMongoClient,pymongo.mongo_client.MongoClient):
                myMongoClient.close()
    finally:
        if 'myMongoClient' in locals():
            if isinstance(myMongoClient,pymongo.mongo_client.MongoClient):
                myMongoClient.close() #Close DB connection  
                functions.logMessage('Closing DB connection...')
# =============================================================================
# Function mergeDictionary
# Merge values from a dictionary into mongo DB, based on key values
# @collection Mongo DB collection object
# @replace object
#               -query: list of columns to match the join
#               -value: name of the column to be inserted
# @row pandas.core.series.Series Row
# =============================================================================
def mergeColumn(collection,replace,row):
    try:
        if not all([collection,replace]): #Checks if any of the parmeters is empty
            raise customError("Empty function parameters")
        if 'query' not in replace:
            raise customError("Empty query parameters")
        if (len(replace['query'])<1): #Checks if any values on replacement dictionary
            raise customError("merge keys cannot be empty")   
        myquery = {}
        for col in replace['query']:
            myquery[col] = row[col]
        value = replace['value']
        newvalues = { "$set": { value: row[value] } } #creates new column with new value
        results = collection.update_many(myquery, newvalues)
        rows = int(results.modified_count)
        if rows > 0:
            functions.logMessage('Updated {} records {}-{} = {}.'.format(rows,replace['query'][0],replace['query'][1],row[value]),1)
        else:
            functions.logMessage("No documents found for {}-{} = {}".format(replace['query'][0],replace['query'][1],row[value]),4)
    except Exception as e:
        functions.logMessage(str(e),2)

