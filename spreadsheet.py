import requests as req
import json
import os
from google.oauth2 import service_account
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build




def main():


    def get_api_creds():

        with open("google_api_creds.json", "r") as file:

            creds= json.loads(file.read())



        return creds

    def fetch_leetcode_data():

        '''This is going to need to return probably a json so that I can deconstruct it into a list to feed to the spreadsheet append function'''

        with open("leetcode.ini", "r") as file:

            file= file.read()
            file= file.split("\n").split(" : ")

        print(file)


        session= req.Session()





        return None

    def get_spreadsheet_info():

        with open("spreadsheet_info.json") as file:

            ss_info= json.loads(file.read())

        return ss_info

    credentials= service_account.Credentials.from_service_account_info(get_api_creds())

    def ss_append(some_data, api_creds):

        s_id= get_spreadsheet_info()

        range_name= "A4:G4"

        try:

            service= build('sheets', 'v4', credentials= api_creds)

            values= [[1, 'string', 99, 3.14, True, "test"]]
            body= {
                    "values": values
                   }

            result= service.spreadsheets().values().append(spreadsheetId= s_id["id"], range= range_name, valueInputOption= "USER_ENTERED", body= body).execute()

            print(f"{(result.get('updates').get('updatedCells'))} cells appended.")

            return result

        except HttpError as error:

            print(f"An error has occurred {error}")

            return error


    #ss_append(None, credentials) # this just calls the append function with some bullshit I made up to test it. Totally meaningless.

    fetch_leetcode_data()




    return None


if __name__ == "__main__":

    main()
