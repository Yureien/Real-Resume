<script lang="ts">
	import Icon from '@iconify/svelte';
	import { Link, Card } from '$lib/components';
	import type { PageData } from './$types';

	export let data: PageData;
</script>

<div class="flex flex-col justify-center items-center text-center relative lg:pt-32 pb-32 lg:pb-64">
	<img
		src="/images/IITKGP-Main-Building.svg"
		alt="Background"
		class="absolute inset-y-0 left-1/2 -translate-x-1/2 h-5/6 -z-10 opacity-10"
	/>
	<h1 class="text-4xl font-bold font-serif" style:text-shadow="2px 2px rgb(191 219 254)">
		&#8220;You are not a resume,
		<br />
		you are a story waiting to be told&#8221;
	</h1>
	<div class="text-justify mt-10 xl:px-48 bg-white/50">
		The rationale while creating this project was pretty clear: that
		<b>you’re way more than what ends up in one piece of paper</b>. So we began the quest of finding
		the “Real Resumes”. That's why we’re asking IIT Kharagpur's students and alumni to submit “Real
		Resumes” where they answer prompts about who they are outside of their resume.
	</div>
	<div class="flex flex-col lg:flex-row items-center gap-8 mt-10 text-2xl">
		<Link href="https://forms.gle/H21pmSAisNDmdEX2A" class="text-blue-700 bg-white/50"
			>Submit Resume</Link
		>
		<Link href="/resume" isButton class="flex items-center">
			View All
			<Icon icon="material-symbols:arrow-right-alt-rounded" class="ml-2" />
		</Link>
	</div>
</div>

<div class="py-16">
	<h1 class="text-4xl font-semibold">Recently Added</h1>
	<div
		class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-4 gap-8 mt-10"
	>
		{#each data.resumes as resume, i}
			<Card
				href="/resume/{resume.id}"
				name={resume.name}
				batch={resume.graduationYear}
				department={resume.department}
				number={i}
				hall={resume.hall}
				image={resume.image}
			/>
		{/each}
	</div>
</div>

<div class="w-1/2 h-1 mx-auto bg-black" />

<div class="py-16">
	<h1 id="about" class="text-4xl font-semibold">About Us</h1>
	<p class="mt-4 text-justify">
		The Project Real Resume aims to change the conversation of what defines success at the Indian
		Institute of Technology, Kharagpur and normalise the struggles that individuals face in their
		academic and professional efforts. The particular problem that the authors felt that there’s too
		much halo around the breakthroughs of the so called accomplished folks and less clarity on their
		“true” journey.
	</p>
	<h3 class="mt-2 text-lg font-semibold">
		Want to fill out your Real Resume?
		<Link class="text-blue-700" href="https://forms.gle/H21pmSAisNDmdEX2A">Fill the form now!</Link>
	</h3>
	<h3 class="mt-4 text-lg">
		Got questions?
		<Link isButton href="mailto:contact@sohamsen.me?subject=Project Real Resume">Contact Us</Link>
	</h3>
	<div class="grid grid-cols-1 md:grid-cols-2 gap-10 mt-10">
		<a href="https://www.linkedin.com/in/samarth-singh-2003/">
			<div
				class="flex flex-col justify-center items-center py-6 px-10
		shadow-[5px_5px] hover:shadow-[10px_10px] shadow-yellow-400 
		bg-white transition-shadow w-full text-center border-2 h-full
		durating-300 ease-out rounded-lg border-black hover:shadow-yellow-400
		"
			>
				<div
					class="w-36 h-36 md:w-40 md:h-40 rounded-3xl
						shadow-[6px_5px] shadow-blue-400 border-2 border-black
						bg-cover bg-center bg-[url('/images/samarth-singh.jpeg')]"
				/>
				<h1 class="mt-6 mb-2 text-3xl font-semibold">Samarth Singh</h1>
				<h3 class="text-gray-500 text-xl font-medium">2025 | MF | RP</h3>
			</div>
		</a>
		<a href="https://sohamsen.me/">
			<div
				class="flex flex-col justify-center items-center py-6 px-10
		shadow-[5px_5px] hover:shadow-[10px_10px] shadow-yellow-400 
		bg-white transition-shadow w-full text-center border-2 h-full
		durating-300 ease-out rounded-lg border-black hover:shadow-yellow-400
		"
			>
				<div
					class="w-36 h-36 md:w-40 md:h-40 rounded-3xl
						shadow-[6px_5px] shadow-blue-400 border-2 border-black
						bg-cover bg-center bg-[url('/images/soham-sen.jpeg')]"
				/>
				<h1 class="mt-6 mb-2 text-3xl font-semibold">Soham Sen</h1>
				<h3 class="text-gray-500 text-xl font-medium">2024 | IE | RP</h3>
			</div>
		</a>
		<a href="https://www.linkedin.com/in/samyak-jain-b09095208/">
			<div
				class="flex flex-col justify-center items-center py-6 px-10
		shadow-[5px_5px] hover:shadow-[10px_10px] shadow-purple-400 
		bg-white transition-shadow w-full text-center border-2 h-full
		durating-300 ease-out rounded-lg border-black hover:shadow-purple-400
		"
			>
				<div
					class="w-36 h-36 md:w-40 md:h-40 rounded-3xl
						shadow-[6px_5px] shadow-amber-600 border-2 border-black
						bg-cover bg-center bg-[url('/images/samyak-jain.jpeg')]"
				/>
				<h1 class="mt-6 mb-2 text-3xl font-semibold">Samyak Jain</h1>
				<h3 class="text-gray-500 text-xl font-medium">2025 | MF | RP</h3>
			</div>
		</a>
		<a href="https://www.linkedin.com/in/vedant-zope/">
			<div
				class="flex flex-col justify-center items-center py-6 px-10
		shadow-[5px_5px] hover:shadow-[10px_10px] shadow-purple-400 
		bg-white transition-shadow w-full text-center border-2 h-full
		durating-300 ease-out rounded-lg border-black hover:shadow-purple-400
		"
			>
				<div
					class="w-36 h-36 md:w-40 md:h-40 rounded-3xl
						shadow-[6px_5px] shadow-amber-600 border-2 border-black
						bg-cover bg-center bg-[url('/images/vedant-zope.jpeg')]"
				/>
				<h1 class="mt-6 mb-2 text-3xl font-semibold">Vedant Zope</h1>
				<h3 class="text-gray-500 text-xl font-medium">2024 | MT | RP</h3>
			</div>
		</a>
	</div>
</div>
