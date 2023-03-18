import { db } from '$lib/database';
import { collection, query, orderBy, limit, getDocs } from 'firebase/firestore';

interface Resume {
	id: string;
	name: string;
	hall: string;
	department: string;
	graduationYear: number;
	image: string;
}

export async function load() {
	const resumeRef = collection(db, 'resume');
	const q = query(resumeRef, orderBy('graduationYear', 'desc'), orderBy('createdAt', 'desc'));
	const queryData = await getDocs(q);

	let data: { [key: string]: Resume[] } = {};

	queryData.forEach((doc) => {
		const { name, hall, department, graduationYear, image } = doc.data();

		if (!data[graduationYear]) data[graduationYear] = [];
		data[graduationYear].push({
			id: doc.id,
			name,
			hall,
			department,
			graduationYear,
			image
		});
	});

	return {
		batches: data
	};
}
