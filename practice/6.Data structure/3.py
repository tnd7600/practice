# create chunks of size n from a list and reverse them

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
chunk_size = len(sample_list)//3
start = 0
stop = chunk_size
for i in range(chunk_size):
    chunk = slice(start, stop)
    chunk_list = sample_list[chunk]
    print(f"Chunk {i+1} : {chunk_list}")
    print(f"After reversing it : {list(reversed(chunk_list))}\n")
    start = stop
    stop += chunk_size