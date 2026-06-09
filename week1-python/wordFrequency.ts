function wordFrequency(sentence: string): Record<string, number> {
    const filteredSentence = sentence.toLowerCase().split(" ")
    //console.log(filteredSentence)
    const wordCount: Record<string, number> = {}
    for (const item of filteredSentence) {
        wordCount[item] = (wordCount[item] || 0) + 1
    }
    return wordCount
}

console.log(wordFrequency("the cat sat on the mat the cat"))