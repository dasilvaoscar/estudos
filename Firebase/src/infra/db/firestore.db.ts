import { FIREBASE_CONFIG } from '../config/firebase.config';
import { initializeApp } from 'firebase/app';
import { getFirestore, collection, getDocs, addDoc } from 'firebase/firestore';

const app = initializeApp(FIREBASE_CONFIG);
const db = getFirestore(app);

export const getFirebaseCollection = async (collectionName: string) => {
  const docs = [];
  const firebaseCollection = collection(db, collectionName);
  const query = await getDocs(firebaseCollection);
  query.forEach((doc) => docs.push(doc.data()));
  return docs;
};

export const addDocumentOnCollection = async (
  collectionName: string,
  doc: object,
) => {
  const firebaseCollection = collection(db, collectionName);
  const query = await addDoc(firebaseCollection, doc);
  return { id: query.id };
};
