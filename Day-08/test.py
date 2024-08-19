s3_buckets = ["bucket1", "bucket2", "bucket3", "bucket4", "bucket5", "bucketBad"]
s3_buckets.append("bucketGood")
s3_buckets.remove("bucketBad")
print(s3_buckets)
sliced = s3_buckets[0:2]
print("This is sliced list: ", sliced)