
interface Employee { name: string, age: number, salary: number }


function printEmployee(employee: Employee[]): void {
    for (const e of employee) {
        console.log(`${e.name} earns ${e.salary}`)
    }
}

function filterBySalary(employee: Employee[], minSalary: number): Employee[] {
    const result: Employee[] = []
    for (const e of employee) {
        if (e.salary > minSalary) {
            result.push(e)
        }

    }
    return result
}


const emp: Employee[] = [{ name: "vivek", age: 26, salary: 25 },
{ name: "pruthvi", age: 19, salary: 20 },
{ name: "Kayagurala", age: 23, salary: 11 }
]

printEmployee(emp)
const aboveMinSalary = filterBySalary(emp, 15)
console.log(aboveMinSalary)

// const result = printEmployee(emp)
// console.log(result)