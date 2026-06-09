function vowelCounter(word: string): number {
    const lowerCaseWord = word.toLowerCase()
    //const splittedWord = lowerCaseWord.split("")
    //console.log(splittedWord)
    let count = 0
    const vowels = ["a", "e", "i", "o", "u"]
    for (const item of lowerCaseWord) {
        if (vowels.includes(item)) {
            count = count + 1
        }

    }
    return count
}

console.log(vowelCounter("Hello World"))
console.log(vowelCounter("TypeScript"))
console.log(vowelCounter("aeiou"))