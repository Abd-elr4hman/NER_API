# Installation and Running API

## Using pip
In your python env run
```
cd to submission/challenge/web
pip install -r requirements.txt
python src/waitress_server.py 
```
## Using docker

### Build your own containers
make sure docker is installed on your system, open terminal and run the following commands
```
cd to submission/challenge
docker-compose up  
```

### Use the saved docker images
Use the docker images in the dir submission/docker-images


# Using API 
- Navigate to your browser and go to http://localhost:5000/
- Upload a file with format of one of the following('.txt')
	- Upload a text file to extract NER from the text.

 


