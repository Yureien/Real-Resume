<script>
	import '../app.css';
	import Icon from '@iconify/svelte';

	import { Link } from '$lib/components';
</script>

<div
	class="fixed w-full items-center bg-white z-50
		grid grid-cols-2 px-10 py-4 shadow"
>
	<div class="col-span-1">
		<a href="/">
			<h1 class="md:text-2xl">
				<span
					class="text-xl block md:inline md:text-4xl font-bold"
					style:text-shadow="2px 2px rgb(191 219 254)"
				>
					Real Resume
				</span>
			</h1>
		</a>
	</div>
	<div class="col-span-1 justify-self-end">
		<div class="flex items-center gap-8">
			<Link href="/" class="hidden md:block">Home</Link>
			<Link href="/#about" class="hidden md:block">About</Link>
			<Link href="/resume" isButton class="flex items-center">
				View All
				<Icon icon="material-symbols:arrow-right-alt-rounded" class="ml-2" />
			</Link>
		</div>
	</div>
</div>

<div class="pt-32 px-4 md:px-24 lg:px-36 xl:px-48">
	<slot />
</div>

<div class="mt-10 py-4 text-center text-gray-600">
	Made with <Icon icon="mdi:heart" class="inline text-red-500" /> in
	<Link class="text-black" href="http://iitkgp.ac.in">IIT Kharagpur</Link>
	<br />
	by Samarth, Soham, Samyak and Shivin
</div>
