from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
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
        USER = 'aacuser'
        PASS = 'GMV_cs340'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30461
        DB = 'aac'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    # Complete this create method to implement the C in CRUD.
    def create(self, data) -> bool:
        if data is not None:
            try:
                # Insert the data parameter into the collection and,
                # assign result with the insert_one operation result
                result = self.database.animals.insert_one(data)  # data should be dictionary
                return result.acknowledged  # return the operation status flag
            except Exception as e:
                print("insert_one failed!")  # Something went wrong so print an error message
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    # Create method to implement the R in CRUD.
    def read(self, data) -> list:
        if data is not None:
            try:
                # Search the collection for the given data
                # The query result will be a cursor
                result = self.database.animals.find(data)  # data should be dictionary
                return list(result)  # Return the cursor transformed into a list
            except Exception as e:
                print("find failed!")  # Something went wrong so print an error message
                return []  # Return an empty list
        else:
            raise Exception("Nothing to find, because data parameter is empty")
