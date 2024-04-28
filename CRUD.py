#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from pymongo import MongoClient
from bson.objectid import ObjectId

#Christopher King
#CS-340
#4/6/2024

class AnimalShelter(object):

	def __init__(self, USER, PASS):
		# Initializing the MongoClient. this helps to
		# access the MongoDB databases and collections.
		# This is hard-wired to use the aac database, the
		# animals collection, and the aac user.
		# Definitions of the connection string variables are
		# unique to the individual Apporto enviroment.
		#
		# You must edit the connection variables below to reflect
		# your own instance of MongoDB!
		#
		# Connection variables
		#USER = 'aacuser'
		#PASS = 'SNHU1234'
		HOST = 'nv-desktop-services.apporto.com'
		PORT = 30879
		DB = 'AAC'
		COL = 'animals'
		#
		# Initialize Connection
		#
		self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
		self.database = self.client['%s' % (DB)]
		self.collection = self.database['%s' % (COL)]
		print("Connection Successful")
        

# Complete this create method to implement the C in CRUD.
	def create(self, data):
		if data is not None:
			self.database.animals.insert_one(data)    # data should be dictionary
			return True
		else:
			raise Exception("Nothing to save, because data parameter is empty")
			return False
        
            
# Create method to implement the R in CRUD.
	def read(self, data):
		if data:
			cursor = self.database.animals.find(data, {"_id": False})
			return cursor
            
		else:
			return self.database.animals.find(data)
        
# Create method to implement the U in CRUD.
	def update(self, searchData, updateData):
		if searchData is not None:
			if self.database.animals.count_documents(searchData, limit =10) !=0:
				update_result = self.database.animals.update_many(searchData, {"$set": updateData})
				result = update_result.raw_result
			else:
				result = "Document not found"
			return result
		else:
			raise Exception("Nothing to update, because data parameter is empty")
			
# Create method to implement the D in CRUD.
	def delete(self, remove):
		if remove is not None:
			if self.database.animals.count_documents(remove, limit = 10) !=0:
				delete_result = self.database.animals.delete_many(remove)
				result = delete_result.raw_result
			else:
				result = "Document not found"
			return result
		else:
			raise Exception("Nothing to delete because data parameter is empty")
