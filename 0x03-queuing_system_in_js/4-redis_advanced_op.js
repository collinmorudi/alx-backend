import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

const hashKey = 'HolbertonSchools';
const schools = {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2,
};

Object.keys(schools).forEach((school) => {
  client.hset(hashKey, school, schools[school], redis.print);
});

client.hgetall(hashKey, (err, result) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(result);
});
