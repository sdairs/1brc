/** @type {import('./$types').PageLoad} */
export async function load({ params, fetch }) {
    let res = await fetch('/api/tinybird/stations', {
        method: 'GET',
        headers: {
            'content-type': 'application/json'
        }
    });
    let stations = await res.json();

    return {
        stations
    };
}