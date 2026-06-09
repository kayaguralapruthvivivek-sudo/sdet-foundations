function filterLongNames(names: string[]): string[] {
    let result = []
    for (const item of names) {
        if (item.length > 5) {
            result.push(item)
        }
    }
    return result
}


console.log(filterLongNames(["Vivek", "Pruthvi", "Kayagurala", "Bob", "Alexander"]))
