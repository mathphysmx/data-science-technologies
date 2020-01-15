# https://sunscrapers.com/blog/elasticsearch-with-python-7-tips-and-best-practices/
# https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html
# https://code-maven.com/python-elasticsearch
# https://elasticsearch-dsl.readthedocs.io/en/latest/

from datetime import date, timedelta

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from elasticsearch_dsl import Document, Text, Date

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

################33

from datetime import date

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from elasticsearch_dsl import Document, Text, Date

es = Elasticsearch()

class EventDocument(Document):
   name = Text
   when = Date

   class Index:
       name = 'events'


docs = []
for i in range(100):
   document = EventDocument(name=f'Sample event {i}', when=date.today())
   docs.append(document.to_dict(include_meta=True))


bulk(es, docs)