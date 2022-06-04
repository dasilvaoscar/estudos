import { FIREBASE_CONFIG } from '../config/firebase.config';
import { initializeApp } from 'firebase/app';
import { getFirestore, collection, getDocs } from 'firebase/firestore';

const app = initializeApp(FIREBASE_CONFIG);
const db = getFirestore(app);

export const getFirebaseCollection = async (collectionName: string) => {
  const docs = [];
  const firebaseCollection = collection(db, collectionName);
  const query = await getDocs(firebaseCollection);
  query.forEach((doc) => docs.push(doc));
  return docs;
};
