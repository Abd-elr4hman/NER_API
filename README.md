# Named-Entity-Recognition-API
a RESTful API to extract named entities (English) from a text file

## Installation and Running Locally

### Using pip
In your python env run
```
cd to submission/challenge/web
pip install -r requirements.txt
python src/waitress_server.py 
```
### Using docker

#### Build your own containers
make sure docker is installed on your system, open terminal and run the following commands
```
cd to submission/challenge
docker-compose up  
```

## Local Run
- Navigate to your browser and go to http://localhost:5000/
- Upload a file with format of one of the following('.txt')
	- Upload a text file to extract NER from the text.
