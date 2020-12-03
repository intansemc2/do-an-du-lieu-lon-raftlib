# coding=utf8

# Tài liệu tham khảo:
# 
# Streaming cơ bản, dùng pyspark.streaming: https://spark.apache.org/docs/latest/streaming-programming-guide.html

import sys

from pyspark import SparkContext
from pyspark.streaming import StreamingContext


if __name__ == "__main__":
    # Tạo một local StreamingContext với 2 luồng và batch sẽ được gọi mỗi 1 giây 
    sc = SparkContext("local[2]", "NetworkWordCount")
    ssc = StreamingContext(sc, 1)

    ##############################################

    # Tạo một DStream chứa các line liên kết đến localhost:9999
    lines = ssc.socketTextStream("localhost", 9999)

    # Tách các từ ra
    counts = lines.flatMap(lambda x: x.split(' '))

    # Pha map
    counts = counts.map(lambda x : (x, 1))

    # Pha reduce
    counts = counts.reduceByKey(lambda a, b: a + b)

    # In kết quả ra màn hình   
    counts.pprint(9999) # Sẽ in ra tối đa số dòng truyền vào, mặc định là 10 

    ##############################################

    ssc.start()             # Bắt đầu tính toán 
    ssc.awaitTermination()  # Chờ cho đến khi kết thúc 
