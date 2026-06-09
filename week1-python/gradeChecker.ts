function getGrade(score: number): string {
    if (score >= 90) {
        return "A"
    }
    else if (score >= 80) {
        return "B"
    }
    else if (score >= 70) {
        return "C"
    }
    else if (score >= 60) {
        return "D"
    }
    else {
        return "F"
    }

}

console.log(getGrade(95))
console.log(getGrade(83))
console.log(getGrade(72))
console.log(getGrade(61))
console.log(getGrade(45))