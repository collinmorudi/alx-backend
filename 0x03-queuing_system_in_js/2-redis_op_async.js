import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

function setNewSchool(schoolName, value, callback) {
  client.set(schoolName, value, redis.print);
  callback();
}

const getAsync = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
  const value = await getAsync(schoolName);
  console.log(value);
}

displaySchoolValue('Holberton')
  .then(() => {
    setNewSchool('HolbertonSanFrancisco', '100', () => {
      displaySchoolValue('HolbertonSanFrancisco');
    });
  });
