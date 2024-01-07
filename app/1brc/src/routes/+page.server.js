/** @type {import('./$types').PageLoad} */
export async function load({ params, fetch }) {
    let stations = await fetch('/api/tinybird/stations', {
        method: 'GET',
        headers: {
            'content-type': 'application/json'
        }
    }).then(r => r.json()).then(r => r.data);

    return {
        stations
    };
}