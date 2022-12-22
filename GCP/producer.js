const { PubSub } = require("@google-cloud/pubsub");

const pubsub = new PubSub({
  projectId: "project-test",
  apiEndpoint: "http://localhost:8432",
});

async function createMessage() {
  pubsub.topic('test').publishMessage({
    json: { name: 'Oscar' },
  })
}

createMessage()