# Named-Entity-Recognition-API
a RESTful API to extract named entities (English) from a text file using [bert-base-NER](https://huggingface.co/dslim/bert-base-NER). Impelemnted with flask. 

## Installation and Running Locally
Download the model file from [here](https://drive.google.com/drive/folders/13nEVxIuxWSqj2dTyGfkIVePr24o0dJlh?usp=sharing) and place it in 
```
./web/src
```
### Using pip
In your python env run
```
cd Named-Entity-Recognition-API/web
pip install -r requirements.txt
python src/waitress_server.py 
```
### Using docker

#### Build your own containers
Run the following commands
```
cd to Named-Entity-Recognition-API
docker-compose up  
```

## Local Run
- Navigate to your browser and go to http://localhost:5000/
- Upload a file with format of one of the following('.txt')
	- Upload a text file to extract NER from the text.
