async function getData() {
    const res = await fetch("http://localhost:5000/api/deals");
    if (!res.ok) {
        throw new Error("Failed to fetch data!");
    }

    return res;
}

export default async function getDeals() {
    const data = await getData();
    return data.json();
}
