<script>
	import { Label, Select } from 'flowbite-svelte';
	let selected;

	let countries = [
		{ value: 'us', name: 'United States' },
		{ value: 'ca', name: 'Canada' },
		{ value: 'fr', name: 'France' }
	];
</script>

<Label>
	(Optional) Filter by station
	<Select class="mt-2" items={countries} bind:value={selected} />
</Label>
