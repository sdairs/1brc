<script>
	import { Select, Button } from 'flowbite-svelte';
	export let selected;

	export let stations = [{ name: 'Loading stations...', value: 'none' }];
</script>

<div class="md:columns-2 columns-1">
	<Select
		items={stations.map((element) => ({
			...element,
			value: element.name
		}))}
		placeholder="Optional station filter"
		bind:value={selected}
	/>
	<Button
		color="red"
		class="w-full md:mt-0 mt-2"
		on:click={() => {
			selected = '';
		}}>Clear</Button
	>
</div>
