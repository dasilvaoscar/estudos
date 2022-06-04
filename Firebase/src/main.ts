import { getFirebaseCollection } from './infra/db/firestore.db';

const collection = 'colecao_teste';

getFirebaseCollection(collection).then(console.log)
