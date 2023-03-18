<script lang="ts">
	export let isButton: boolean = false;
	export let href: string;
	let className: string = '';
	export { className as class };
</script>

{#if isButton}
	<a
		{href}
		class="shadow-[5px_5px] shadow-blue-700 border-2 border-black
			transition-colors ease-out duration-300 hover:text-white
			bg-gradient-to-r hover:from-gray-900 hover:to-black
			from-white to-gray-100 py-2 px-4 rounded
			text-black {className}"
	>
		<slot />
	</a>
{:else}
	<a
		{href}
		class="relative before:content-[''] before:absolute
    before:w-full before:h-[2px] before:bottom-0 before:left-0 before:bg-black
    before:hover:scale-x-100 before:scale-x-0 before:origin-top-left
    before:transition before:ease-in-out before:duration-300 {className}"
	>
		<slot />
	</a>
{/if}
