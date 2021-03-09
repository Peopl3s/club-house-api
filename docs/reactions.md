# Reactions

Before that setup the default client, or will inject your own client.

## Creating

```python
id_story = 125
id_comment = 127
new_reation = {'emoji': ':-)'}
reaction = await club_house.stories.create(id_story, 'comments', 
                                           id_comment, 'reactions',
                                           **new_reation)
```


## Delete

When None is returned this means it was successfull

```python
id_story = 125
id_comment = 127
reation = {'emoji': ':-)'}
reaction = await club_house.stories.delete(id_story, 'comments', 
                                           id_comment, 'reactions',
                                           **reation)
```
