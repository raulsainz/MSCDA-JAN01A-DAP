# =============================================================================
# Created By  : Raul Sainz
# Created Date: 2021-03-21
# =============================================================================
"""The Module Has Been Build for DAP Project"""
# =============================================================================
# Imports
# =============================================================================
import psycopg2                   #Library for setting up the connection to PostgreSQL
import psycopg2.extras as extras  #Miscellaneous goodies for Psycopg2
import urllib                     #Library to url encode the password
import os                         #os library to interact with host OS
import math
import pandas as pd
from  mypackage.functions import logMessage
from  mypackage.classes import customError
# =============================================================================
# DB Configuration variables
# =============================================================================
DB_SERVER = 'ncirl-az01.westeurope.cloudapp.azure.com'
DB_PORT   =  5432
DB_NAME   = 'remotedap'
DB_USER   = 'remotedap2'
DB_PWD    = 'Hola1234'

# =============================================================================
# Function to connect to PostgreSQL
# Provides connection object to PostgreSQL
# @returns: psycopg2.extensions.connection
# =============================================================================

def getPSQLClient():  
    logMessage("Connecting to PostgeSQL ...".format())
    try:
        conn = psycopg2.connect(
                                    host     = DB_SERVER,
                                    database = DB_NAME,
                                    user     = DB_USER,
                                    password = DB_PWD,
                                    port     = DB_PORT)
        return conn
    except Exception as e:
        logMessage(str(e),2)
        return 1

# =============================================================================
# Get PostgreSQL DB tables information summary
# @returns:print list of tables with number or rows
# =============================================================================
def getDBStatistics():
    conn = getPSQLClient()
    try:
        # Open a cursor to perform database operations
        command = '''select n.nspname as table_schema,
                    c.relname as table_name,
                    c.reltuples as rows
                    from pg_class c
                    join pg_namespace n on n.oid = c.relnamespace
                    where c.relkind = 'r'
                    and n.nspname not in ('information_schema','pg_catalog')
                    order by c.reltuples desc;'''
        cursor = conn.cursor()
        cursor.execute(command);
        rows = cursor.fetchall()
        for row in rows:
            logMessage("Table: {} - Rows: {}".format(row[1],row[2]),4)
    except psycopg2.Error as e:
        conn.rollback()
        logMessage(e.pgerror,2)
        return 1
    except (Exception, psycopg2.DatabaseError) as error:
        conn.rollback()
        logMessage("Error: {}".format(error),2)
        return 1
    
    finally:
        logMessage("Closing DB connection...".format())
        cursor.close()
        conn.close()
# =============================================================================
# Upload a data frame to PostgreSQL using psycopg2.extras.execute_values() to insert the dataframe
# @returns:print list of tables with number or rows
# =============================================================================
def uploadDataFrame(df, table):
    #Connect to DB
    conn = getPSQLClient()
    cursor = conn.cursor()
    # Create a list of tupples from the dataframe values
    tuples = [tuple(x) for x in df.to_numpy()]
    # Comma-separated dataframe columns
    cols = ','.join(list(df.columns))
    # SQL quert to execute
    query  = "INSERT INTO %s(%s) VALUES %%s" % (table, cols)   
    try:
        # Open a cursor to perform database operations
        logMessage("Inserting {} into table {}...".format(len(tuples),table),4)
        
        extras.execute_values(cursor, query, tuples)
        updated_rows = cursor.rowcount
        logMessage("Finish inserting - Affected rows: {}".format(updated_rows),1)
        conn.commit()
    except psycopg2.Error as e:
        conn.rollback()
        logMessage(e.pgerror,2)
        return 
    except (Exception, psycopg2.DatabaseError) as error:
        conn.rollback()
        logMessage("Error: {}".format(error),2)
        return
    
    finally:
        logMessage("Closing DB connection...".format())
        cursor.close()
        conn.close()


def getTableToDataframe(table):
    #Tranform a SELECT query into a pandas dataframe
    conn = getPSQLClient()
    cursor = conn.cursor()
    column_names = []
    try:
        # Create query to get table column names
        column_query = "SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = '%s'" % (table)
        cursor.execute(column_query)
        rows= cursor.fetchall()
        for row in rows:
            column_names.append(row[0])
        # Get Table rows
        select_query  = "SELECT * FROM %s " % (table)
        logMessage('Queryng table {} ...'.format(table))
        cursor.execute(select_query)
        # Extract list of tupples from cursor response
        tupples = cursor.fetchall() 
        # Plug tuples into pandas dataframe
        df = pd.DataFrame(tupples,columns=column_names)
        logMessage("Sucesfully importred {} into dataframe columns: {} - rows: {}".format(table,df.shape[1],df.shape[0]),1)
        return df
    except (Exception, psycopg2.DatabaseError) as error:
        logMessage("Error: %s" % error,2)
        cursor.close()
        conn.close()
    finally:
        logMessage("Closing DB connection...".format())
        del df
        cursor.close()
        conn.close()


# =============================================================================
# Upload a data frame to PostgreSQL using psycopg2.extras.execute_values() to insert the dataframe
# @returns:print list of tables with number or rows
# =============================================================================
def createTable(table_name,drop_table=False):
    #Connect to DB
    conn = getPSQLClient()
    # SQL quert to execute
    if drop_table:
        logMessage("Dropping table {} !!!".format(table_name),3)
        drop_command = 'DROP TABLE IF EXISTS {};'.format(table_name)
    else:
        drop_command = ''
    command =  '''{}
            CREATE TABLE  {}(
            _id SERIAL PRIMARY KEY,
            month character(4),
            age_group varchar(255),
            education varchar(255),
            employement varchar(255),
            marital varchar(255),
            state_death character(4),
            type_death varchar(255),
            place_death varchar(255),
            icd10_desc varchar(255),
            icd10_code varchar(3),
            icd10_group varchar(7),
            icd10_chapter varchar(7),
            is_male boolean,
            is_work_related  boolean,
            is_foreign boolean,
            is_pregnant boolean,
            is_accident boolean,
            is_cancer boolean,
            is_CVD boolean,
            is_diabetes boolean,
            is_digestive boolean,
            is_mental boolean,
            is_pregnancy boolean,
            is_respiratory boolean,
            is_virus boolean,
            is_suicide boolean,
            is_bacteria boolean
            )
            '''.format(drop_command,table_name)
    try:
        logMessage("Creating table {} ...".format(table_name),4)
        cursor = conn.cursor()
        cursor.execute(command);
        conn.commit()
    except psycopg2.Error as e:
        conn.rollback()
        logMessage(e.pgerror,2)
        return 1
    except (Exception, psycopg2.DatabaseError) as error:
        conn.rollback()
        logMessage("Error: {}".format(error),2)
        return 1
    
    finally:
        logMessage("Closing DB connection...".format())
        cursor.close()
        conn.close()
