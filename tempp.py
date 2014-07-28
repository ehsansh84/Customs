from tools.redis import Redis

Redis.set('name', value='ehsan')
print(Redis.get('name'))