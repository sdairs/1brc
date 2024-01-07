<script>
	import { Card, Button, Blockquote } from 'flowbite-svelte';
	import ResultTable from '../components/ResultTable.svelte';
	import StationSelect from '../components/StationSelect.svelte';
	import ResultStats from '../components/ResultStats.svelte';
	import { onMount } from 'svelte';

	/** @type {import('./$types').PageData} */
	export let data;

	let batch_station_filter = undefined;
	let realtime_station_filter = undefined;
	let batch_results = [];
	let batch_stats = {};
	let batch_loading = false;
	let realtime_results = [];
	let realtime_loading = false;
	let realtime_stats = {};
	let realtime_row_count = 0;
	let realtime_ingest_error = false;
	let realtime_ingest_has_sent = false;

	let realtime_elapsed = 'Press Go!';
	let batch_elapsed = 'Press Go!';
	async function quick_go() {
		realtime_elapsed = 'Running...';
		batch_elapsed = 'Running...';
		run(1).then((res) => {
			batch_elapsed = res.statistics.elapsed.toString() + 's';
		});
		run().then((res) => {
			realtime_elapsed = res.statistics.elapsed.toString() + 's';
		});
	}

	async function run_button(batch = false) {
		let results = await run(batch).then((res) => res);
		if (batch) {
			batch_loading = true;
			batch_results = results.data;
			batch_stats = results.statistics;
			batch_loading = false;
		} else {
			realtime_loading = true;
			realtime_results = results.data;
			realtime_stats = results.statistics;
			realtime_loading = false;
		}
	}

	async function run(batch = false) {
		let url = '/api/tinybird/aggregate';
		if (batch) {
			url += '?type=batch';
			if (batch_station_filter) {
				url += '&station=' + batch_station_filter;
			}
		} else {
			console.log('realtime');
			if (realtime_station_filter) {
				url += '?station=' + realtime_station_filter;
			}
		}
		console.log(url);
		let result = fetch(url, {
			headers: {
				accept: 'application/json'
			}
		}).then((res) => res.json());
		return result;
	}

	async function update_streaming_row_count(delay = false) {
		if (delay) await new Promise((r) => setTimeout(r, 1000));
		let result = await fetch('/api/tinybird/row_count', {
			headers: {
				accept: 'application/json'
			}
		}).then((res) => res.json());
		realtime_row_count = result.data[0].row_count;
	}

	async function ingest_rows() {
		let result = await fetch('/api/tinybird/ingest', {
			headers: {
				accept: 'application/json'
			}
		}).then((res) => res.json());
		if (result == 202) {
			realtime_ingest_has_sent = true;
			update_streaming_row_count(true);
		} else {
			realtime_ingest_error = true;
		}
		return result;
	}

	onMount(async () => {
		update_streaming_row_count(false);
	});
</script>

<main class="prose prose-xl mx-auto pb-48">
	<h1 class="mt-8">1brc 1️⃣🐝🏎️</h1>
	<p>
		<a href="https://github.com/gunnarmorling/1brc">1brc challenge</a> from
		<a href="https://github.com/gunnarmorling">@gunnarmorling</a>
	</p>
	<Blockquote
		>The One Billion Row Challenge (1BRC) is a fun exploration of how far modern Java can be pushed
		for aggregating one billion rows from a text file. Grab all your (virtual) threads, reach out to
		SIMD, optimize your GC, or pull any other trick, and create the fastest implementation for
		solving this task!</Blockquote
	>
	<p>
		Although originally a Java optimisation challenge, it's an analytics problem, so I wanted to
		solve it using <a href="https://tinybird.co">Tinybird</a>. While Tinybird can solve the problem
		pretty quickly even in batch, it can be solved super efficiently as a realtime/streaming
		problem, too.
	</p>
	<Button href="https://github.com/sdairs/1brc" color="dark" size="xl" class="w-full"
		>View on GitHub</Button
	>
	<div>
		<h2>Quick results</h2>
		<div>
			<Button class="w-full my-2" color="green" on:click={quick_go}
				>{#if !batch_loading}Go! 1️⃣🐝🏎️{:else}Loading...{/if}</Button
			>
		</div>
		<div class="md:columns-2 columns-1">
			<div>
				<Card>
					<h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">
						Batch
					</h5>
					<p class="font-normal text-gray-700 dark:text-gray-400 leading-tight">{batch_elapsed}</p>
				</Card>
			</div>
			<div>
				<Card class="md:mt-0 mt-2">
					<h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">
						Realtime
					</h5>
					<p class="font-normal text-gray-700 dark:text-gray-400 leading-tight">
						{realtime_elapsed}
					</p>
				</Card>
			</div>
		</div>
	</div>
	<div>
		<h2>Playground</h2>
		<p>
			Hit the run buttons to execute the queries. By default, no filters are applied, aggregating
			for all 413 stations. Filter for a single station using the selector (this applies a WHERE
			clause and re-executes the query, to show you how efficient filtering is).
		</p>
		<p>
			There have been <b>{realtime_row_count}</b> measurements ingested through the streaming source,
			while the batch source remains at a static 1 billion.
		</p>
		<div>
			<h3>Batch</h3>
			<p>
				The batch method re-runs the three aggregations over all 1 billion raw rows. This is highly
				in-efficient, although it still only takes ~3 seconds to complete using Tinybird (based on
				ClickHouse).
			</p>
			<form>
				<StationSelect
					class="w-full"
					stations={data.stations}
					bind:selected={batch_station_filter}
				/>
				<Button class="w-full mt-2" size="xl" color="green" on:click={() => run_button(true)}
					>{#if !batch_loading}EXECUTE BATCH{:else}Loading...{/if}</Button
				>
			</form>
			<div>
				<ResultStats stats={batch_stats} />
			</div>
			<div class="h-96 overflow-y-scroll border mt-2">
				<ResultTable items={batch_results} />
			</div>
		</div>
		<div>
			<h3>Realtime</h3>
			<p>
				The realtime meathod uses a continuous, event-driven materialized view to aggregate rows at
				ingestion time. This is a native feature of Tinybird/ClickHouse, and is highly efficient.
				All 1 billion rows have been ingested and pre-aggregated, so executing the query simply
				serves the pre-aggregated results. Ingesting new rows will automatically, and incrementally,
				update the existing aggregations.
			</p>
			<form>
				<StationSelect
					class="w-full"
					stations={data.stations}
					bind:selected={realtime_station_filter}
				/>
				<Button class="w-full mt-2" size="xl" color="green" on:click={() => run_button(false)}
					>{#if !realtime_loading}EXECUTE REALTIME{:else}Loading...{/if}</Button
				>
			</form>
			<Button color="yellow" class="w-full mt-2" size="xl" on:click={ingest_rows}>
				{#if realtime_ingest_error}
					Failed 😭 Try again? 🚀
				{:else if !realtime_ingest_has_sent}
					{realtime_row_count} rows - send more? 🚀
				{:else}
					{realtime_row_count} rows - SEND MORE? 🚀
				{/if}
			</Button>
			<div>
				<ResultStats stats={realtime_stats} {realtime_row_count} />
			</div>
			<div class="h-96 overflow-y-scroll border mt-2">
				<ResultTable items={realtime_results} />
			</div>
		</div>
	</div>
</main>
