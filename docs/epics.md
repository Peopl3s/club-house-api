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

## Create Epic Comment 

```python
id_epic = 113
id_author = '6028be51'
new_comm = {'author_id': id_author, 'text': 'new comment'}
comment = await club_house.epics.create(id_epic, 'comments', **new_comm)
```

## Get Epic Comment 

```python
id_epic = 113
id_comment = 114
comment = await club_house.epics.get(id_epic, 'comments', id_comment)
```

## Update Epic Comment

```python
id_epic = 113
id_comment = 114
updated_fields_comm = {'text': 'changed text'}
comment = await club_house.epics.update(id_epic, 'comments', id_comment,
                                                    **updated_fields_comm)
```

## Create Epic Comment Comment

```python
id_epic = 113
id_comment = 114
new_comm = {'text': 'sub comment'}
comment = await club_house.epics.create(id_epic, 'comments', id_comment, **new_comm)
```

## Delete Comment

```python
id_epic = 113
id_comment = 114
await club_house.epics.delete(id_epic, id_comment)
```

## List Epic Comments

```python
list_comment_of_epic = await club_house.epics(id_epic, 'comments')
```

## List Epic Stories

```python
list_stories_of_epic = await club_house.epics(id_epic, 'stories')
```

