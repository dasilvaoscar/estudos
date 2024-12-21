import type { CreateTableCommandInput } from "@aws-sdk/client-dynamodb";
import { dynamoClient } from "./shared";

async function listTables() {
  try {
    console.log("Fetching tables...");
    const tables = await dynamoClient.listTables({});
    console.log("Tables:", tables.TableNames);
  } catch (err) {
    console.error("Error listing tables:", err);
  }
}

export async function createTable() {
  try {
    await listTables()

    const params: CreateTableCommandInput = {
      TableName: "TestTable",
      KeySchema: [
        { AttributeName: "id", KeyType: "HASH" },
      ],
      AttributeDefinitions: [
        { AttributeName: "id", AttributeType: "S" },
      ],
      ProvisionedThroughput: {
        ReadCapacityUnits: 1,
        WriteCapacityUnits: 1,
      },
    };

    const result = await dynamoClient.createTable(params);
    console.log("Table created successfully:", result);
  } catch (err) { }
}