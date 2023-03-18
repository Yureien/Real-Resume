<script lang="ts">
	import Icon from '@iconify/svelte';
	import type { PageData } from './$types';

	export let data: PageData;
</script>

{#if data === undefined}
	<h1 class="text-4xl text-center">Loading ...</h1>
{:else if !data.success}
	<h1 class="text-4xl text-center">Error</h1>
	{#if data.error}<p class="mt-4 text-xl text-center">{data.error}</p>{/if}
{:else}
	<div
		class="pb-16 my-16 px-2 md:px-10 pt-20 lg:pt-6 relative w-full bg-slate-100 rounded-3xl
	lg:shadow-[24px_20px] shadow-[6px_5px] shadow-yellow-300 lg:shadow-yellow-300"
	>
		<div
			class="absolute rounded-xl md:shadow-[10px_10px] shadow-sky-300 bg-cover bg-center
		-top-12 left-1/2 right-0 -translate-x-1/2 lg:left-auto lg:right-12 lg:translate-x-0
		lg:-top-16 w-28 h-28 lg:w-64 lg:h-64 border-2 border-black bg-white
		shadow-[4px_4px] md:shadow-sky-300"
			style:background-image="url('{data.image}')"
		/>
		<div class="lg:mr-80 flex flex-col lg:flex-row items-center lg:items-baseline lg:justify-start">
			<h1 class="text-3xl md:text-5xl font-semibold text-center lg:text-left w-full">
				{data.name}
			</h1>
			<h5 class="text-sm md:text-xl text-gray-700 text-center lg:text-left w-fit whitespace-nowrap">
				{data.department} | {data.graduationYear} | {data.hall}
			</h5>
		</div>
		<div class="flex gap-2 justify-center lg:justify-start">
			{#if data.linkedin}
				<a href={data.linkedin} target="_blank" rel="noreferrer">
					<Icon
						icon="mdi:linkedin"
						class="inline-block text-gray-600 hover:text-black transition-colors duration-300 w-6 h-6"
					/>
				</a>
			{/if}
			{#if data.email}
				<a href="mailto:{data.email}" target="_blank" rel="noreferrer">
					<Icon
						icon="mdi:email"
						class="inline-block text-gray-600 hover:text-black transition-colors duration-300 w-6 h-6"
					/>
				</a>
			{/if}
			{#if data.facebook}
				<a href={data.facebook} target="_blank" rel="noreferrer">
					<Icon
						icon="mdi:facebook"
						class="inline-block text-gray-600 hover:text-black transition-colors duration-300 w-6 h-6"
					/>
				</a>
			{/if}
			{#if data.instagram}
				<a href={data.instagram} target="_blank" rel="noreferrer">
					<Icon
						icon="mdi:instagram"
						class="inline-block text-gray-600 hover:text-black transition-colors duration-300 w-6 h-6"
					/>
				</a>
			{/if}
			{#if data.website}
				<a href={data.website} target="_blank" rel="noreferrer">
					<Icon
						icon="mdi:web"
						class="inline-block text-gray-600 hover:text-black transition-colors duration-300 w-6 h-6"
					/>
				</a>
			{/if}
		</div>
		<div class="lg:mr-80 max-md:px-4 text-sm xl:text-base mt-2 md:mt-4 text-justify">
			{data.description}
		</div>

		{#if data.LsTaken.length > 0}
			<div
				class="rounded-xl mt-4 py-4 md:py-6 mx-4 md:mx-0 md:mt-6 xl:mt-12 px-4 md:px-8 bg-white
		md:shadow-[10px_10px] shadow-orange-500 shadow-[4px_4px] md:shadow-orange-500 border-2 border-black"
			>
				<h1 class="text-xl md:text-4xl md:mb-10 font-semibold">L&#8217;s Taken</h1>

				{#each data.LsTaken as { title, items }, idx}
					<div
						class="grid grid-cols-12 gap-x-1 sm:gap-x-2 md:gap-x-10 my-4 w-full pb-4
				{idx !== data.LsTaken.length - 1 ? 'border-b-2' : ''}"
					>
						<h1
							class="col-span-3 sm:col-span-2 text-3xl md:text-5xl 
				text-center font-semibold text-sky-700 w-full"
						>
							{items.length}
						</h1>
						<h1 class="col-span-9 lg:col-span-10 text-lg md:text-2xl font-medium text-sky-700">
							{title}
						</h1>
						<div class="col-start-2 lg:col-start-3 mt-4 md:mt-2 col-span-11 lg:col-span-10">
							<ul class="text-sm md:text-lg list-outside ml-4 list-disc space-y-1">
								{#each items as item}
									<li>{item}</li>
								{/each}
							</ul>
						</div>
					</div>
				{/each}
			</div>
		{/if}

		{#if data.BrightSide.length > 0}
			<div
				class="rounded-xl mt-4 py-4 md:py-10 mx-4 md:mx-0 md:mt-6 xl:mt-12 px-4 md:px-8 bg-white
	shadow-[4px_4px] shadow-pink-400 md:shadow-[10px_10px] md:shadow-pink-400 border-2 border-black"
			>
				<h1 class="text-xl md:text-4xl mb-4 font-semibold">On the Bright Side</h1>

				{#each data.BrightSide as { title, items }, idx}
					<div
						class="grid grid-cols-12 gap-x-1 sm:gap-x-2 md:gap-x-10 my-4 w-full pb-4
				{idx !== data.BrightSide.length - 1 ? 'border-b-2' : ''}"
					>
						<h1
							class="col-span-3 sm:col-span-2 text-3xl md:text-5xl 
				text-center font-semibold text-sky-700 w-full"
						>
							{items.length}
						</h1>
						<h1 class="col-span-9 lg:col-span-10 text-lg md:text-2xl font-medium text-sky-700">
							{title}
						</h1>
						<div class="col-start-2 lg:col-start-3 mt-4 md:mt-2 col-span-11 lg:col-span-10">
							<ul class="text-sm md:text-lg list-outside ml-4 list-disc space-y-1">
								{#each items as item}
									<li>{item}</li>
								{/each}
							</ul>
						</div>
					</div>
				{/each}
			</div>
		{/if}

		{#if data.noContextImage}
			<div
				class="rounded-xl mt-4 py-4 md:py-10 mx-4 md:mx-0 md:mt-6 xl:mt-12 px-4 md:px-8 bg-white
md:shadow-[10px_10px] shadow-purple-500 shadow-[4px_4px] md:shadow-purple-500 border-2 border-black"
			>
				<h1 class="text-xl md:text-4xl mb-4 font-semibold">Photo Wall</h1>
				<img
					src={data.noContextImage}
					alt="No Context"
					class="w-full rounded-3xl border-2 border-black"
				/>
			</div>
		{/if}
	</div>
{/if}
