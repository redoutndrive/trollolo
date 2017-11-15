from django.db import models
import uuid


class Board(models.Model):
    boardTitle = models.TextField(max_length=50, blank=False, unique=True)
    boardDescription = models.TextField(max_length=500, blank=True)


class Table(models.Model):
    tableTitle = models.TextField(max_length=50, blank=False, unique=True)
    tableDescription = models.TextField(max_length=500, blank=True)
    boardID = models.ForeignKey(Board, on_delete=models.CASCADE)


class Card(models.Model):
    archiveStatus = models.BooleanField(default=False)
    title = models.TextField(max_length=200, blank=False)
    description = models.TextField(max_length=1000, blank=True)
    uniqueNumber = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    tableID = models.ForeignKey(Table, on_delete=models.CASCADE)




