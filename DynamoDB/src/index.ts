import { PutCommand, GetCommand,  } from "@aws-sdk/lib-dynamodb";

import { createTable } from "./create-table";
import { dynamoClient } from "./shared";


export async function getItem(tableName: string, key: object) {
  const command = new GetCommand({
    TableName: tableName,
    Key: key,
  });

  try {
    const response = await dynamoClient.send(command);
    return response.Item;
  } catch (error) {
    console.error("Erro ao obter item:", error);
  }
}


export async function createItem(tableName: string, item: object) {
  const command = new PutCommand({
    TableName: tableName,
    Item: item,
  });

  console.log('Comando pronto')

  try {
    await dynamoClient.send(command);
    console.log("Item criado com sucesso:", item);
  } catch (error) {
    console.error("Erro ao criar item:", error);
  }
}

async function execute() {
  await createTable()

  await createItem('TestTable', { id: 'test-1', a: 2 })
  const item = await getItem('TestTable', { id: 'test' })

  console.log('ITEM', item)
}

execute()