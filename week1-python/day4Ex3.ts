async function fetchUser(userId: number): Promise<object> {
    await new Promise(resolve => setTimeout(resolve, 3000))
    return { id: userId, name: "Vivek", address: "Texas" }
}

async function fetchOrders(userId: number): Promise<object> {
    await new Promise(resolve => setTimeout(resolve, 2000))
    return { id: userId, orders: 3 }
}

async function fetchPayments(userId: number): Promise<object> {
    await new Promise(resolve => setTimeout(resolve, 1000))
    return { id: userId, PaymentType: "card" }
}

async function main(): Promise<void> {
    console.log("start:", new Date().toLocaleTimeString())
    //const result = await Promise.all([fetchUser(1), fetchOrders(1), fetchPayments(1)])
    const user = await fetchUser(1)
    const orders = await fetchOrders(1)
    const payments = await fetchPayments(1)
    console.log("End:", new Date().toLocaleTimeString())
    console.log(user, orders, payments)
}
main()