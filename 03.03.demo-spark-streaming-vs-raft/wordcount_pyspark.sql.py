# coding=utf8

# Tài liệu tham khảo:
# 
# Streaming sử dụng query trong pyspark.sql, in kết quả nhìn đẹp hơn: http://spark.apache.org/docs/latest/structured-streaming-programming-guide.html

import sys

from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.functions import split


if __name__ == "__main__":
    # Khởi tạo Spark 
    spark = SparkSession.builder.appName("StructuredNetworkWordCount").getOrCreate()

    ##############################################

    # Tạo một Dataframe chứa các line liên kết đến localhost:9999
    lines = spark.readStream.format("socket").option("host", "localhost").option("port", 9999).load()

    # Tách các line thành các từ 
    words = lines.select(
       explode(
           split(lines.value, " ")
       ).alias("word")
    )

    # Đếm từ 
    wordCounts = words.groupBy("word").count()

    # In kết quả ra console 
    query = wordCounts.writeStream.outputMode("complete").format("console").start()

    ##############################################

    query.awaitTermination() # Chờ cho đến khi kết thúc 
