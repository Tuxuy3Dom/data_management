let companies = `[
    {
        "name": "Big Boss",
        "numberOfEmployees": 100000,
        "ceo": "Mary",
        "rating": 3.0
    },
    {
        "name": "Small Boss",
        "numberOfEmployees": 3,
        "ceo": null,
        "rating": 4.0
    }
]`

console.log(JSON.parse(companies)[1].name)