import { db } from '$lib/database';
import { doc, getDoc } from 'firebase/firestore';

export async function load({ params }: { params: { id: string } }) {
	const docRef = doc(db, 'resume', params.id);
	const docSnap = await getDoc(docRef);

	if (!docSnap.exists()) {
		return {
			success: false,
			error: 'No such document!'
		};
	}

	const data = docSnap.data();
	const {
		name,
		hall,
		department,
		graduationYear,
		bio: description,
		linkedin,
		facebook,
		instagram,
		website,
		displayEmail: email,
		LsTaken,
		BrightSide,
		image,
		noContextImage
	} = data;

	return {
		success: true,
		id: params.id,
		image: image ?? 'https://upload.wikimedia.org/wikipedia/commons/2/2c/Default_pfp.svg',
		noContextImage,
		name,
		hall,
		graduationYear,
		department,
		description,
		linkedin,
		facebook,
		instagram,
		website,
		email,
		LsTaken,
		BrightSide
	};
}
