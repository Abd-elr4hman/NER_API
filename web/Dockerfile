FROM python:3.8
WORKDIR /NER_API

# Copy all my files to container
ADD . /NER_API

# Install dependancies
RUN pip install -r requirements.txt

EXPOSE 5000

CMD /challenge/run.sh
