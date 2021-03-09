# Labels

Before that setup the default client, or will inject your own client.

## Creating

```python
new_label = {'name': 'first label'}
label = await club_house.labels.create(**new_label)
```

## Updating

```python
id_label = 116
updated_fields_label= { 'name': 'Label updated now'}
label = await club_house.labels.update(id_label, **updated_fields_label)
```

## Get by id

```python
id_label = 116
label = await club_house.labels.get(id_label)
#epic = await club_house.labels(id_epic) alternative 
print(label)
```

## Deleting by id

When None is returned this means it was successfull

```python
id_label = 116
await club_house.labels.delete(id_label)
```

## Listing

Returns a list of all labels

```python
list_labels = await club_house.labels()
```

## List Label Epics

```python
id_label = 14
epics = await club_house.labels.get(id_label, 'epics')
#epics = await club_house.labels(id_label, 'epics')
```

## List Label Stories

```python
id_label = 14
stories = await club_house.labels(id_label, 'stories')
#stories = await club_house.labels.get(id_label, 'stories')
```

