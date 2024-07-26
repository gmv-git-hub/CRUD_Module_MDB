from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, user, psw):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        # USER = 'aacuser'
        # PASS = 'GMV_cs340'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30461
        DB = 'aac'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (user, psw, HOST, PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    # Method to implement the Create in CRUD.
    def create(self, data: dict) -> bool:
        if data is not None:
            try:
                # Insert the data parameter into the collection and,
                # assign result with the insert_one operation result
                result = self.database.animals.insert_one(data)  # data should be dictionary
                return result.acknowledged  # return the operation status flag
            except Exception as e:
                print(f"insert_one failed: {e}")  # Something went wrong so print an error message
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    # Method to implement the Read in CRUD.
    def read(self, search_filter: dict) -> list:
        if search_filter is not None:
            try:
                # Search the collection for the given data
                # The query result will be a cursor
                result = self.database.animals.find(search_filter)  # data should be dictionary
                return list(result)  # Return the cursor transformed into a list
            except Exception as e:
                print(f"find failed: {e}")  # Something went wrong so print an error message
                return []  # Return an empty list
        else:
            raise Exception("Nothing to find, because filter parameter is empty")

    # Method to implement the Update in CRUD.
    def update(self, search_filter: dict, data: dict) -> int:
        if search_filter is not None and data is not None:
            try:
                # Modify the documents that satisfy the filter with the given data
                # The query result will be a cursor that can be used to have the
                # number of documents modified, filter and data should be dictionary
                result = self.database.animals.update_many(search_filter, {'$set': data})
                return result.matched_count  # Extract the number of modified document from the cursor
            except Exception as e:
                print(f"update failed: {e}")  # Something went wrong so print an error message
                return 0  # Return an empty list
        else:
            raise Exception("Missing filter or data parameter")

    # Method to implement the Delete in CRUD.
    def delete(self, search_filter: dict) -> int:
        if search_filter is not None:
            try:
                # Remove the documents that satisfy the given filter
                # The query result will be a cursor that can be used to have the
                # number of delete documents, filter should be dictionary
                result = self.database.animals.delete_many(search_filter)
                return result.deleted_count  # Extract the number of deleted document from the cursor
            except Exception as e:
                print(f"delete failed: {e}")  # Something went wrong so print an error message
                return 0  # Return an empty list
        else:
            raise Exception("Nothing to delete, because filter parameter is empty")
