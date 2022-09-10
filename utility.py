import json
import traceback

from pymongo import MongoClient


class MongoDBUtility(object):
    def __init__(self, mongo_host, mongo_port, user_name=None, password=None):
        try:
            self.__mongo_OBJ__ = MongoClient(
                host=mongo_host,
                port=mongo_port,
                username=user_name,
                password=password
            )

        except Exception as e:
            raise Exception(str(e))

    def insert_one(self, json_data, database_name, collection_name):
        try:
            mongo_response = self.__mongo_OBJ__[database_name][collection_name].insert_one(
                json_data)
            try:
                self.__mongo_OBJ__.close_connection()
            except Exception as e:
                pass
            return mongo_response.inserted_id
        except Exception as e:
            traceback.print_exc()
            try:
                self.__mongo_OBJ__.close_connection()
            except Exception as e:
                pass
            raise Exception(str(e))

    def find_with_condition(self, json_data, database_name, collection_name):
        try:
            database_connection = self.__mongo_OBJ__[database_name]
            mongo_response = database_connection[collection_name].find(json_data)
            try:
                self.__mongo_OBJ__.close_connection()
            except Exception as e:
                pass
            return mongo_response
        except Exception as e:
            traceback.print_exc()
            try:
                self.__mongo_OBJ__.close_connection()
            except Exception as e:
                pass
            raise Exception(str(e))

    def update_one(self, condition, json_data, database_name, collection_name):
        try:
            database_connection = self.__mongo_OBJ__[database_name]
            database_connection[collection_name].update_one(condition, {"$set": json_data})
            try:
                self.__mongo_OBJ__.close_connection()
            except Exception as e:
                pass
            return "success"
        except Exception as e:
            traceback.print_exc()
            try:
                self.__mongo_OBJ__.close_connection()
            except Exception as e:
                pass
            raise Exception(str(e))

    def __del__(self):
        self.__mongo_OBJ__.close()


class FileReader(object):
    def __init__(self):
        ""

    @staticmethod
    def file_reader():
        with open("config.json", 'r') as file:
            config = json.loads(file.read())
        return config
