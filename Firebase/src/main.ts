import {
  getFirebaseCollection,
  addDocumentOnCollection,
} from './infra/db/firestore.db';

const collection = 'colecao_teste';

addDocumentOnCollection(collection, { nome: 'teste' }).then(console.log);
getFirebaseCollection(collection).then(console.log);
