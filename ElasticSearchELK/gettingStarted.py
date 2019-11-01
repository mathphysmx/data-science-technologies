# https://sunscrapers.com/blog/elasticsearch-with-python-7-tips-and-best-practices/
# https://code-maven.com/python-elasticsearch
# https://elasticsearch-dsl.readthedocs.io/en/latest/

from datetime import date, timedelta

from elasticsearch import Elasticsearch

es = Elasticsearch()


doc = {
   'internal_id': 123,
   'name': 'Jazz concert',
   'category': 'concert',
   'where': 'Warsaw',
   'when:': date.today(),
   'duration_hours': 2,
   'is_free': False,
}


es.index(index='events', body=doc)

es.indices.get_mapping(index='events')