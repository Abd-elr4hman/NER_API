# Named-Entity-Recognition-API
a RESTful API to extract named entities (English) from text using [bert-base-NER](https://huggingface.co/dslim/bert-base-NER). Implemented with flask. 

## Run Locally
Download the model file from [here](https://drive.google.com/drive/folders/13nEVxIuxWSqj2dTyGfkIVePr24o0dJlh?usp=sharing) and place it in:
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

## test locally 
```
curl --header "Content-Type: application/json"  --request POST   --data '{"instances":["my name is Ahmed I live in Germany"]}' http://localhost:5000/predict
```
