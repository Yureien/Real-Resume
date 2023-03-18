import { initializeApp } from 'firebase/app';
// import { getAnalytics } from "firebase/analytics";
import { getFirestore } from 'firebase/firestore';

const firebaseConfig = {
	apiKey: 'AIzaSyBJvCNwgogAa6-0xI8WNp3cj2AUYvdymG4',
	authDomain: 'project-real-resume.firebaseapp.com',
	projectId: 'project-real-resume',
	storageBucket: 'project-real-resume.appspot.com',
	messagingSenderId: '677743442363',
	appId: '1:677743442363:web:566a30637ae8e606be6c9e',
	measurementId: 'G-VMCR90GX5E'
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

// Initialize Cloud Firestore and get a reference to the service
export const db = getFirestore(app);
// export const analytics = getAnalytics(app);
