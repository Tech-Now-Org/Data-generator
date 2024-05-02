from dotenv import load_dotenv
import google.generativeai as genai
from pandas import read_json
import os

# load model configuration
model_config = read_json('./model_config.json')

class Model:
    """_summary_ : init gemini mode of communication
    Args:
        mode (str): types of Gemini mode:
            gen (str): for generative text only
            chat (str): for chat session
        text (str): Gemini generated text
        google_api_key (str): google api key 

    Returns:
        text (str): mardown formatted text 
    """
    # Set up the model
    # gemini satefy responce setting

    def __init__(self, key):
       self.key = key
       #configure gemini library
       genai.configure(api_key= self.key)

    def generate(self, data_structure, data_desciption,):
        """_summary_

        Args:
            data_structure (_type_): _description_
            data_desciption (_type_): _description_

        Returns:
            _type_: _description_
        """
        self.data_structure, self.data_desciption = data_structure, data_desciption
        try:
            # Initialize Generative GEMINI Model with its safety settings
            model = genai.GenerativeModel('gemini-pro', generation_config=model_config.generation_config, safety_settings=model_config.safety_settings)
            response = model.generate_content()
            # generated data
            return response.text
        except:
            print('Error occured while generating data!')

    def validate(self, data):
        """_summary_

        Args:
            data (_type_): _description_

        Returns:
            _type_: _description_
        """
        self.data = data
        try:
            # Initialize Generative GEMINI Model
            model = genai.GenerativeModel('gemini-pro', generation_config=model_config.generation_config, safety_settings=model_config.safety_settings)
            response = model.generate_content()
            # validated data
            return response.text
        except:
            print('Error occured while validating data!')   
