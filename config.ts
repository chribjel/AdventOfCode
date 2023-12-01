const URL = "https://adventofcode.com/";


export async function fetchInput(year = new Date().getFullYear(), day = new Date().getDate()) {
    const url = `${URL}${year}/day/${day}/input`;
    const res = await fetch(url, {
        headers: {
            Cookie: `session=${process.env.SESSION}`
        }
    });
    const text = await res.text();
    return text;
}
