import { TINYBIRD_API_KEY } from '$env/static/private';
import { json } from '@sveltejs/kit';


export async function GET({ url }) {
    let tb_url = new URL(`https://api.tinybird.co/v0/pipes/temperature_api.json`)
    let params = new URLSearchParams();
    if (url.searchParams.get("type")) {
        params.append("type", "batch");
    }
    if (url.searchParams.get("station")) {
        params.append("station", url.searchParams.get("station"));
    }
    tb_url.search = params;

    const result = await fetch(tb_url, {
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

