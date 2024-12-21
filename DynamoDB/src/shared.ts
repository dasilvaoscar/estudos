import { DynamoDB } from "@aws-sdk/client-dynamodb";

export const dynamoClient = new DynamoDB({
  region: "us-east-1",
  endpoint: "http://localhost:8000",
  credentials: {
    accessKeyId: "fakeAccessKey",
    secretAccessKey: "fakeSecretKey",
    sessionToken: 'fakeSessionToken'
  },
});

