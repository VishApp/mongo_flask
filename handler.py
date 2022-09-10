import traceback

from utility import MongoDBUtility

from utility import FileReader

config = FileReader().file_reader()


class CreateUser:
    def __init__(self):
        self.mongo_obj = MongoDBUtility(mongo_host=config["mongo_host"], mongo_port=config["mongo_port"])

    def create_user(self, user_name, password, age):
        try:
            result = self.mongo_obj.find_with_condition({"username": user_name}, database_name="user_db",
                                                        collection_name="user_details")
            if len(list(result)) > 0:
                self.mongo_obj.update_one({"username": user_name},
                                          {"username": user_name, "password": password, "age": age},
                                          database_name="user_db",
                                          collection_name="user_details")

            else:
                self.mongo_obj.insert_one({"username": user_name, "password": password, "age": age},
                                          database_name="user_db",
                                          collection_name="user_details")

            return {"status": "success"}
        except Exception as e:
            traceback.print_exc()
            return {"status": "failed"}
