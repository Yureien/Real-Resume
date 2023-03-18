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
	const q = query(resumeRef, orderBy('createdAt', 'desc'), limit(4));
	const queryData = await getDocs(q);

	const data: Resume[] = [];

	queryData.forEach((doc) => {
		const { name, hall, department, graduationYear, image } = doc.data();
		data.push({
			id: doc.id,
			name,
			hall,
			department,
			graduationYear,
			image
		});
	});

	return {
		resumes: data
	};
}
