from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

def process_text(file):
    # Open text file 
    with open(file, 'r') as f:
        # Save text in Contents
        Contents = f.read()
    
    # Initialize tokenizer
    tokenizer = AutoTokenizer.from_pretrained("./src/bert-base-NER")
    
    # Initialize Model
    model = AutoModelForTokenClassification.from_pretrained("./src/bert-base-NER")
    
    # Initialize Pipeline
    nlp = pipeline("ner", model=model, tokenizer=tokenizer)

    # Run prediction 
    ner_results = nlp(Contents)

    return str(ner_results)  # Return result as string

