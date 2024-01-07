import { TINYBIRD_API_KEY } from '$env/static/public';


export async function GET() {
    let url = new URL(`https://api.tinybird.co/v0/pipes/get_stations.json`);

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
        console.table(result.data)
        console.log("** Query columns **")
        for (let column of result.meta) {
            console.log(`${column.name} -> ${column.type}`)
        }
        return result;
    }
}

