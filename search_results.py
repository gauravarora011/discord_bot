import json
import requests
import os

def set_google_search_request_parameters(search_query):
    """To Set up the request parameters for GET Query"""
    params = {}
    params['key'] = os.environ.get('discordapp_google_key')
    params['cx'] = os.environ.get('discordapp_google_cx')
    params['q'] = search_query
    return params

def find_google_results(search_query):
    """ To find the google results for a particular string and format the results"""
    URL =  'https://www.googleapis.com/customsearch/v1'
    params = set_google_search_request_parameters(search_query)
    result_data = requests.get(URL,params = params).content
    result_data_dict = json.loads(result_data)
    formatted_data = "Here the following search results from GOOGLE! \n\n"
    for item in result_data_dict['items'][:5]:
        formatted_data += f"{item['title']} \nURL :  {item['link']} \n\n"
    return formatted_data
