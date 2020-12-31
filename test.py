import datastore as ds
import time

# initializing a datastore file without filepath, creates it in current working directory
ds.datastore()

# creating a key-value pair
ds.create("Vishal", {"FreshWorks": 10}, 3)

# reading the value for a given key
print(ds.read("Vishal"))

# Timeout functionality check
i = 1
while i < 7:
    print(ds.read("Vishal"), end=' ')  # reads the key every second
    print("in", i, "second")
    time.sleep(1)
    i += 1

# deleting the created pair
ds.delete("Vishal")
print(ds.read("Vishal"))