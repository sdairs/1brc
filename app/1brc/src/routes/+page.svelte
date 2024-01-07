<script>
	import { Card, Button } from 'flowbite-svelte';
	import ResultTable from '../components/ResultTable.svelte';
	import StationSelect from '../components/StationSelect.svelte';
	import { onMount } from 'svelte';

	const btn1 = () => {
		alert('You clicked btn1.');
	};

	let items = [
		{ id: 1, maker: 'Toyota', type: 'ABC', make: 2017 },
		{ id: 2, maker: 'Ford', type: 'CDE', make: 2018 },
		{ id: 3, maker: 'Volvo', type: 'FGH', make: 2019 },
		{ id: 4, maker: 'Saab', type: 'IJK', make: 2020 }
	];

	let stations;
	onMount(() => {
		stations = fetch('/api/tinybird/stations')
			.then((res) => res.json())
			.then((data) => {
				console.log(data.data);
			});
	});
</script>

<main class="prose prose-xl mx-auto">
	<h1 class="mt-8">1brc 1️⃣🐝🏎️</h1>
	<p>1brc challenge from etc etc</p>
	<h2>Batch</h2>
	<p>Challenge done in batch etc etc</p>
	<StationSelect {stations} />
	<Button color="green" on:click={btn1}>Run batch 1️⃣🐝🏎️</Button>
	<div class="py-8">
		<Card>
			<h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">
				Query time
			</h5>
			<p class="font-normal text-gray-700 dark:text-gray-400 leading-tight">0 ms</p>
		</Card>
	</div>
	<ResultTable {items} />
	<h2>Realtime</h2>
	<p>Challenge done in realtime etc etc</p>
	<StationSelect {stations} />
	<Button color="green" on:click={btn1}>Run realtime 1️⃣🐝🏎️</Button>
	<div class="py-8">
		<Card>
			<h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">
				Query time
			</h5>
			<p class="font-normal text-gray-700 dark:text-gray-400 leading-tight">0 ms</p>
		</Card>
	</div>
	<ResultTable {items} />
</main>
