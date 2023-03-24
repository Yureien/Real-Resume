<script lang="ts">
	import { Card } from '$lib/components';
	import type { PageData } from './$types';

	export let data: PageData;
</script>

{#each Object.keys(data.batches).sort((a, b) => Number(b) - Number(a)) as year}
	<div class="pb-16">
		<h1 class="text-2xl">Batch of <span class="text-4xl ml-2 font-semibold">{year}</span></h1>
		<div class="grid grid-cols-1 md:grid-cols-4 gap-8 mt-10">
			{#each data.batches[year] as resume, i}
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
{/each}
