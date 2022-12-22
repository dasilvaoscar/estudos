const { PubSub } = require("@google-cloud/pubsub");

const pubsub = new PubSub({
  projectId: 'project-test',
  apiEndpoint: 'http://localhost:8432'
});

async function listener() {
  console.log('Waiting message')

  const server = pubsub.subscription('test')
  
  server.on("message", (message) => {
    console.log("Received message:", message.data.toString());
  });
  
  server.on("error", (error) => {
    console.error("Received error:", error);
  });
}

setInterval(listener, 1000)