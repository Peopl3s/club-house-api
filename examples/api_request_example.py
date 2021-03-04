from club_house_api import ClubHouse
import asyncio

TOKEN = os.getenv('API_TOKEN')

club_house_session = ClubHouse(TOKEN, 'v3')
club_house = club_house_session.get_api()

async def main():

    all_projects = await club_house.projects()
    first_project_id = all_projects[0]['id']

    new_story = {'name': 'My new story', 'project_id': first_project_id}
    story = await club_house.stories.create(**new_story)
    print(story)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
