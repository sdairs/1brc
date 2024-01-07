<script>
	export let stats;

	function formatBytes(a, b = 2) {
		if (!+a) return '0 Bytes';
		const c = 0 > b ? 0 : b,
			d = Math.floor(Math.log(a) / Math.log(1024));
		return `${parseFloat((a / Math.pow(1024, d)).toFixed(c))} ${
			['Bytes', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB'][d]
		}`;
	}
</script>

<div>
	<p><b>Rows scanned: </b>{stats.rows_read ?? 0}</p>
	<p><b>Data processed: </b>{formatBytes(stats.bytes_read)}</p>
	<p><b>Time elapsed: </b>{stats.elapsed ?? 0}</p>
</div>
