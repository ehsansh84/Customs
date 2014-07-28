from tools.redis import Redis

# Redis.set('name', value='ehsan')
# print(Redis.get('name'))

r = redis_instance
r.set('name', 'ehsan', 1000)