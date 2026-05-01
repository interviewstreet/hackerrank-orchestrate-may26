# Call Sower's Solution

## My approach

1. Create embeddings from the data folder - once - using Sentence Transformers
2. Map the embeddings - at initiation -
3. Embedded the query - ticket row -
4. Get relevant data from the map
5. Send data and the query to the LLM
6. Receive and return the data.

---

## Requirements (check pyproject.toml)

1. [Sentence Transformers](https://sbert.net/)
2. [Google Gemini](https://ai.google.dev/gemini-api/docs)

## Quick Shoutout
I want to thank Boot.dev, Lane Wagner and Isaac Flath for their Learn Retrieval Augmented Generation Course
I owe this app to the stuff I learned from that course.
Obviously I want to thank HackerRank.com for this opportunity

## How it works

### embeddings/embeddings.py

1. check if the data is embedded, if not, build the embeddings, else load the embeddings
2. create a map from the embeddings and the data
3. embed the query - support ticket - get relative data using the ebeddings

### llm/llm.py

1. get the relative data and the query
2. using a prompt get a response from the llm
3. return the response in requested format
