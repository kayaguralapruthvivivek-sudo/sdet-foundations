async function getUserData(userId: number): Promise<object> {
    return { id: userId, name: "Vivek", email: "test@gmail.com" }

}

async function main(): Promise<void> {
    const result = await getUserData(1)
    console.log(result)
}

main()