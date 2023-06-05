import math

def bucket_sort(elements):
    number_of_buckets = round(math.sqrt(len(elements)))
    max_value =  max(elements)
    buckets = [[] for _ in range(number_of_buckets)]
    
    for element in elements:
        bucket = math.ceil(element*number_of_buckets/max_value)
        buckets[bucket-1].append(element)
        
    for bucket in buckets:
        bucket.sort()
        
    return [element for bucket in buckets for element in bucket]

print(bucket_sort([4,2,6,5,1,3]))