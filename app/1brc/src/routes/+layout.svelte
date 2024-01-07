<script>
	import '../app.css';

	/** @type {import('./$types').PageData} */
	export let data;
</script>

<svelte:head>
	{#if data.deploymentEnv === 'production'}
		<script
			src="https://beamanalytics.b-cdn.net/beam.min.js"
			data-token={data.beamKey}
			async
		></script>
	{/if}
</svelte:head>

<slot />
