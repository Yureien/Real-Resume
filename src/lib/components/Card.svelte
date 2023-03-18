<script lang="ts">
	export let href: string;
	export let image: string = 'https://upload.wikimedia.org/wikipedia/commons/2/2c/Default_pfp.svg';
	export let name: string;
	export let batch: string | number;
	export let department: string;
	export let number: number;
	export let hall: string;

	const shadowColors = [
		'shadow-lime-400 hover:shadow-lime-400',
		'shadow-blue-500 hover:shadow-blue-500',
		'shadow-yellow-400 hover:shadow-yellow-400',
		'shadow-red-500 hover:shadow-red-500',
		'shadow-purple-700 hover:shadow-purple-700',
		'shadow-pink-400 hover:shadow-pink-400',
		'shadow-indigo-600 hover:shadow-indigo-600',
		'shadow-gray-400 hover:shadow-gray-400'
	];

	const shadowColor: string = shadowColors[number % shadowColors.length];
</script>

<a {href}>
	<div
		class="flex flex-col justify-start items-center py-6 px-10
	shadow-[5px_5px] hover:shadow-[10px_10px] {shadowColor} border-2
	bg-white transition-shadow w-full text-center h-full
	durating-300 ease-out rounded-lg border-black
	"
	>
		<img src={image} alt="Picture of {name}" class="w-32 h-32 rounded-full border-2 border-black" />
		<h1 class="mt-6 mb-2 text-2xl font-semibold">{name}</h1>
		<h3 class="text-gray-500 font-medium">{batch} | {department} | {hall}</h3>
	</div>
</a>
