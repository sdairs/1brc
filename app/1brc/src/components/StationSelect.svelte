<script>
	import { Label, Select } from 'flowbite-svelte';
	let selected;

	export let stations = [];
</script>

<Label>
	(Optional) Filter by station
	<Select class="mt-2" items={stations} bind:value={selected} />
</Label>
