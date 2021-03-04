# Epics

Before that setup the default client, or will inject your own client.

## Creating

```python
new_epic = { 'name': "Epic One", 
             'description': 'Epic description',
             'state': 'in progress'}
             
epic = await club_house.epics.create(**new_epic)
```

## Updating

```python
id_epic = 112
updated_fields_epic = { 'description': 'Changed description','state': 'done'}
epic = await club_house.epics.update(id_epic, **updated_fields_epic)
```

## Get by id

```python
id_epic = 112
epic = await club_house.epics.get(id_epic)
#epic = await club_house.epics(id_epic) alternative 
print(epic)
```

## Deleting by id

When None is returned this means it was successfull

```python
id_epic = 112
await club_house.epics.delete(id_epic)
```

## Listing

Returns a list of all epics

```python
list_of_epics = await club_house.epics()
```

