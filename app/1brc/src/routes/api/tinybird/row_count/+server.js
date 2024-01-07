import { TINYBIRD_API_KEY } from '$env/static/private';
import { json } from '@sveltejs/kit';


export async function GET() {
    let url = new URL(`https://api.tinybird.co/v0/pipes/streaming_row_count.json`)

    const result = await fetch(url, {
        headers: {
            Authorization: `Bearer ${TINYBIRD_API_KEY}`
        }
    })
        .then(r => r.json())
        .then(r => r)
        .catch(e => e.toString())

    if (!result.data) {
        console.error(`there is a problem running the query: ${result}`);
    } else {
        return json(result);
    }
}