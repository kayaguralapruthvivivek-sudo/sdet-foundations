interface Stats { sum: number, average: number, min: number, max: number }


function listStats(numbers: number[]): Stats {
    let sum: number = 0
    let min = numbers[0]
    let max: number = 0
    for (const i of numbers) {
        sum = sum + i
        if (i > max) {
            max = i
        }

        if (i < min) {
            min = i
        }

    }
    const average = sum / numbers.length
    return { sum, average, min, max }
}

console.log(listStats([10, 25, 12, 18, 5]))
console.log(listStats([100, 200, 300]))
console.log(listStats([5, 1, 8, 3, 9, 2]))

