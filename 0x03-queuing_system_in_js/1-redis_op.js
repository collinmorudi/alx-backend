import redis from 'redis';

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

function displaySchoolValue(schoolName, callback) {
  client.get(schoolName, (err, result) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(result);
    callback();
  });
}

displaySchoolValue('Holberton', () => {
  setNewSchool('HolbertonSanFrancisco', '100', () => {
    displaySchoolValue('HolbertonSanFrancisco', () => {});
  });
});
