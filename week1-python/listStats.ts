interface Stats { sum: number, average: number, min: number, max: number }

function listStats(numbers: number[]): Stats {
    let sum = 0
    let min = numbers[0]
    let max = 0
    for (const item of numbers) {

        sum = sum + item
        if (item > max) {
            max = item
        }
        if (item < min) {
            min = item
        }
    }
    const average = sum / numbers.length

    return { sum, average, min, max }

}

console.log(listStats([10, 20, 30, 0]))
console.log(listStats([1, 3, 5, 2]))
console.log(listStats([3, 6, 9, 1]))