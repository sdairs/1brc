<script>
	import {
		Table,
		TableBody,
		TableBodyCell,
		TableBodyRow,
		TableHead,
		TableHeadCell
	} from 'flowbite-svelte';
	import { writable } from 'svelte/store';

	export let items = [];

	const sortKey = writable('station'); // default sort key
	const sortDirection = writable(1); // default sort direction (ascending)
	const sortItems = writable(items.slice()); // make a copy of the items array

	// Define a function to sort the items
	const sortTable = (key) => {
		// If the same key is clicked, reverse the sort direction
		if ($sortKey === key) {
			sortDirection.update((val) => -val);
		} else {
			sortKey.set(key);
			sortDirection.set(1);
		}
	};

	$: {
		const key = $sortKey;
		const direction = $sortDirection;
		const sorted = [...$sortItems].sort((a, b) => {
			const aVal = a[key];
			const bVal = b[key];
			if (aVal < bVal) {
				return -direction;
			} else if (aVal > bVal) {
				return direction;
			}
			return 0;
		});
		sortItems.set(sorted);
	}
</script>

<Table hoverable={true}>
	<TableHead>
		<TableHeadCell on:click={() => sortTable('id')}>ID</TableHeadCell>
		<TableHeadCell on:click={() => sortTable('maker')}>Maker</TableHeadCell>
		<TableHeadCell on:click={() => sortTable('type')}>Type</TableHeadCell>
		<TableHeadCell on:click={() => sortTable('make')}>Make</TableHeadCell>
	</TableHead>
	<TableBody class="divide-y">
		{#each $sortItems as item}
			<TableBodyRow>
				<TableBodyCell>{item.id}</TableBodyCell>
				<TableBodyCell>{item.maker}</TableBodyCell>
				<TableBodyCell>{item.type}</TableBodyCell>
				<TableBodyCell>{item.make}</TableBodyCell>
			</TableBodyRow>
		{/each}
	</TableBody>
</Table>
