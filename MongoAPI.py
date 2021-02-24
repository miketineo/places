from flask import Flask, request, json, Response
from pymongo import MongoClient
import logging as log
import os

HOST = os.environ.get('DOCKER_HOST_IP', 'localhost')
PORT = os.environ.get('MONGO_PORT', '5000')

class MongoAPI:
    def __init__(self, data):
        log.basicConfig(level=log.DEBUG, format='%(asctime)s %(levelname)s:\n%(message)s\n')
        # self.client = MongoClient("mongodb://localhost:27017/")  # When only Mongo DB is running on Docker.
        self.client = MongoClient("mongodb://%s:%s/"%(HOST, PORT))

        database = data['database']
        collection = data['collection']
        cursor = self.client[database]
        self.collection = cursor[collection]
        self.data = data

    def read(self):
        log.info('Reading All Data')
        documents = self.collection.find()
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output

    def write(self, data):
        log.info('Writing Data')
        new_document = data['Document']
        if isinstance(new_document, list):
            log.info("inserting many")
            response = self.collection.insert_many(new_document)
            inserted = str(response.inserted_ids)
        else:
            response = self.collection.insert_one(new_document)
            inserted = str(response.inserted_id)
        output = {'Status': 'Successfully Inserted',
                  'Document_ID': inserted}
        return output

    def update(self):
        log.info('Updating Data')
        filt = self.data['Filter']
        updated_data = {"$set": self.data['DataToBeUpdated']}
        response = self.collection.update_one(filt, updated_data)
        output = {'Status': 'Successfully Updated' if response.modified_count > 0 else "Nothing was updated."}
        return output

    def delete(self, data):
        log.info('Deleting Data')
        filt = data['Filter']
        if (filt == "*"):
            response = self.collection.drop()
            output = {'Status': 'Successfully Deleted All'}
        else:
            response = self.collection.delete_one(filt)
            output = {'Status': 'Successfully Deleted' if response.deleted_count > 0 else "Document not found."}
        return output

