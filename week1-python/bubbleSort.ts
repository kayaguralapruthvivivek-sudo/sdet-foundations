function bubbleSort(numbers: number[]): number[] {
    for (const item of numbers) {
        for (let i = 0; i < numbers.length - 1; i++) {
            if (numbers[i] > numbers[i + 1]) {
                const swap = numbers[i]
                numbers[i] = numbers[i + 1]
                numbers[i + 1] = swap
            }
        }
    }
    return numbers
}

console.log(bubbleSort([64, 34, 25, 12, 22]))
console.log(bubbleSort([5, 1, 8, 3, 9, 2]))
console.log(bubbleSort([100, 50, 75, 25]))