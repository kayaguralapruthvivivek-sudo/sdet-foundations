function isPalindrome(word: string): boolean {
    const finalWord: string = word.toLowerCase()
    const wordLength: number = word.length
    // console.log(finalWord)
    // console.log(wordLength)
    for (let i = 0; i < wordLength / 2; i++) {
        if (finalWord[i] !== finalWord[wordLength - 1 - i]) {
            return false
        }


    }
    return true
}


// console.log(isPalindrome("racecar"))
console.log(isPalindrome("racecar"))  // true
console.log(isPalindrome("hello"))    // false
console.log(isPalindrome("level"))    // true
console.log(isPalindrome("Nitin"))    // true