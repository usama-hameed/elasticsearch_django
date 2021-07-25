from django.shortcuts import render
from elasticsearch import Elasticsearch
# Create your views here.

es = Elasticsearch(hosts="http://127.0.0.1", port=9200)

def search_movie(request):
    data = []
    final_data ={}
    if request.method == 'POST':
        attribute=request.POST.get('attributes')
        print(attribute)
        value=request.POST.get('value')
        print(value)
        response = movie_search_query(attribute, value)
        for res in response['hits']['hits']:
            data.append(res['_source'])
        for d in data:
            d['Release_Year'] = d['Release Year']
            del d['Release Year']
            d['Wiki_Page'] = d['Wiki Page']
            del d['Wiki Page']
        return render(request, 'response.html',{'data':data})
    return render(request, 'movie_search.html')


def movie_search_query(attribute, value):
    res = es.search(
        index='movies',
        body={
            "query": {
                "match": {
                    attribute: value
                }
            }
        }
    )
    return res