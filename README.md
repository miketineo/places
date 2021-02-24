# Places
Playing around with Python and MongoDB

Just trying to play with Mongo DB, so my idea was to follow this [guide](https://medium.com/@ishmeet1995/how-to-create-restful-crud-api-with-python-flask-mongodb-and-docker-8f6ccb73c5bc) you know I love learning by doing.

So I change a little bit the premise and downloaded a csv full of cities from [Simple Maps](https://simplemaps.com/data/world-cities) and wrote a script to import them but also make the api able to create not just cities 1 by 1 but in bulk.  See the Payloads section

## First thing first
if you want to try this out... you might need to have some stuff set up first.

* Docker
* Mongo docker image
* Mongo Compass (optional but cool to visualize stuff
* Python3.X
* PostMan or Curl Knoledge!

## Docker set up

Nothing Fancy I just 

```
docker pull mongo
docker create -it --name MongoDev -p 5000:27017 mongo
docker start MongoDev
```

## Python 

I guess you can simply use your favorite package manager if you dont have it yet.  Also might need to install `pymong` and `flask`

```
pip install pymongo
pip install flask
```
## Running the app

```
python Mongo.py
```
