# from django.db import models

# Create your models here.

from django.db import models

class Author(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField()

class Article( models.Model ) :

    title = models.CharField( max_length=120 )
    description = models.TextField()
    body = models.TextField()
    # author = models.ForeignKey( 'Author', related_name='articles', on_delete=models.CASCADE)

    def __str__(self) :
        return self.title


import uuid
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel

class ExampleModel(DjangoCassandraModel):
    example_id    = columns.UUID(primary_key=True, default=uuid.uuid4)
    example_type  = columns.Integer(index=True)
    created_at    = columns.DateTime()
    description   = columns.Text(required=False)