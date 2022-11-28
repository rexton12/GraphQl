import asyncio
from prisma import Prisma


async def main() -> None:
    db = Prisma()
    await db.connect()

    post = await db.user.create(
        data={
            'id':'1',
            'firstname': 'Rexton',
            'lastname': 'Itsiah',
            'published': True,
            'desc': 'New member',
        }
    )
    print(f'created User: {post.json(indent=2, sort_keys=True)}')

    found = await db.user.find_unique(where={'id': post.id})
    assert found is not None
    print(f'found user: {found.json(indent=2, sort_keys=True)}')

    await db.disconnect()


if __name__ == '__main__':
    asyncio.run(main())
   