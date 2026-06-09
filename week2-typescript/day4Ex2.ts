async function fetchUserData(userId: number): Promise<object> {

    await new Promise(resolve => setTimeout(resolve, 2000))
    return { id: userId, name: "vivek", salary: 2500 }
}

async function main(): Promise<void> {
    console.log("fetching user ...")
    const result = await fetchUserData(1)
    console.log(result)

}

main()