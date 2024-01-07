/** @type {import('./$types').PageLoad} */
export async function load({ params, fetch }) {
    let res = await fetch('/api/tinybird/stations');
    let stations = await res.json();

    return {
        stations
    };
}