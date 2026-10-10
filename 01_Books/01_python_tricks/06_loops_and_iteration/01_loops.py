l = ["a", "b", "c"]

for i in range(len(l)):
    print(i)


for idx, item in enumerate(l):
    print(idx, item)


emails = {
    "Bob": "bob@example.com",
    "Alice": "alice@example.com",
}

for name, email in emails.items():
    print(name, email)


start = 0
stop = 10
step = 2

for i in range(start, stop, step):
    print(i)
