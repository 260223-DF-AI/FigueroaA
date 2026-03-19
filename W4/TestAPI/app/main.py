from fastapi import FastAPI, Body
from pydantic import BaseModel
import json

app = FastAPI()
loudList = []

class Item(BaseModel):
    my_str: str

@app.get("/")
def get_root():
        """
        Get Root
        
        This is the root of the API, this is a smoke-check to validate the app is acually running at all"""
        return "Hello World"

@app.post("/")
def post_root(my_str: str):
        """
        Post Root

        A simple post request endpoint, to accept a value from the client.
        """
        
        loudList.append(my_str.upper())
        return json.dumps({"Greeting": my_str.upper()})

@app.get("/loudlist")
def get_list():
        return json.dumps({"Loud list" : loudList})

@app.delete("/benslist")
def delete_benslist():
        loudList.clear()
        return json.dumps({"Loud list": loudList})

@app.put("/loudlist/{list_index}")
def update_list(str_update: str, list_index: int):
        """
        Update Loud List

        Simple PUT request to change a value in the list
        """
        loudList[list_index] = str_update
        return json.dumps({"Loud List" : str_update})
        
#www.google.com/
#127.0.0.1

# get
# put
# post
# patch
# delete
# head
# connect
# options

# JSON notation: Javascript Object Notation