
interface TestResult { testName: string, passed: boolean, duration: number }

function getFailedTests(testResults: TestResult[]): TestResult[] {
    const result: TestResult[] = []
    for (const tr of testResults) {
        if (!tr.passed) {
            result.push(tr)
        }
    }
    return result

}

function getSummary(testResults: TestResult[]): void {
    let count: number = 0
    let countFailed: number = 0
    let countPassed: number = 0
    let totalDuration = 0
    for (const tr of testResults) {
        count = count + 1
        totalDuration = totalDuration + tr.duration
        if (!tr.passed) {
            countFailed = countFailed + 1
        }
        else {
            countPassed = countPassed + 1
        }
    }
    const averageDuration: number = totalDuration / count
    console.log(`total number of  tests is ${count}, number of failed tests are  ${countFailed}, number of passed tests are ${countPassed} and average duration of the test is ${averageDuration}`)

}

const testResults: TestResult[] = [{ testName: "chat test", passed: true, duration: 300 },
{ testName: "login test", passed: true, duration: 500 },
{ testName: "checkout test", passed: false, duration: 600 },
{ testName: "payment gateway test", passed: false, duration: 350 },
{ testName: "go live test", passed: true, duration: 200 }
]

const failedStudents = getFailedTests(testResults)
console.log(failedStudents)

getSummary(testResults)