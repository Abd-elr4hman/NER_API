from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
import pathlib

def process_text(Instances_list):

    pathlike = pathlib.Path("./src/bert-base-NER")

    # Initialize tokenizer
    tokenizer = AutoTokenizer.from_pretrained(pathlike)
    
    # Initialize Model
    model = AutoModelForTokenClassification.from_pretrained(pathlike)

    # Initialize Pipeline
    nlp = pipeline("ner", model=model, tokenizer=tokenizer)

    #NER_PREDS= []
    ner_results = nlp(Instances_list)

    return ner_results # Return result as string
