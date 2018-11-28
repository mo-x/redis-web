import redis


class RedisUtil:

    @staticmethod
    def get_conn():
        # noinspection PyBroadException
        try:
            global pool
            # host is the redis host,the redis server and client are required to open, and the redis default port is 6379
            pool = redis.ConnectionPool(host='127.0.0.1', password='myredis', port=6379, decode_responses=True)
            print("connected success.")
            print("could not connect to redis.")
            return redis.Redis(connection_pool=pool)
        except:
            print("connect exception")



