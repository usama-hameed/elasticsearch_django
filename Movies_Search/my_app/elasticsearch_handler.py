from elasticsearch import Elasticsearch
from elasticsearch import helpers
import json

# ES_HOST="http://192.168.18.101"
# ES_PORT=9200
# es = Elasticsearch([{'host': ES_HOST, 'port': ES_PORT}])
es = Elasticsearch(hosts="http://127.0.0.1", port=9200)
print(es.ping())

def full_text_search(keyword, index, field):
    res = es.search(
        index='movies',
        body={
            "query": {
                "match": {
                    field: keyword
                }
            }
        }
    )
    return res


