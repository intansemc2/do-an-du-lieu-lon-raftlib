# coding=utf8

import sys

from pyspark.sql import SparkSession

import pandas
from tabulate import tabulate 

def printOutput(counts):
    output = counts.collect()

    pandas.set_option('display.max_rows', None)
    pandas.set_option('display.max_columns', None)
    pandas.set_option('display.width', None)
    pandas.set_option('display.max_colwidth', -1)

    dataframe = pandas.DataFrame(output, range(len(output)), ["Từ", "Số lần xuất hiện"])
    dataframe.style.set_table_styles([{'selector' : '','props' : [('border','2px solid white')]}]) 

    print("\n\n")
    print("Kết quả:")
    print(tabulate(dataframe, headers = 'keys', tablefmt = 'psql')) 
    print("\n\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: wordcount <file>", file=sys.stderr)
        sys.exit(-1)

    spark = SparkSession.builder.appName("PythonWordCount").getOrCreate()

    lines = spark.read.text(sys.argv[1]).rdd.map(lambda r: r[0])

    ###########################################

    # Tách các từ ra
    counts = lines.flatMap(lambda x: x.split(' '))

    # Pha map
    counts = counts.map(lambda x : (x, 1))

    # Pha reduce
    counts = counts.reduceByKey(lambda a, b: a + b)

    # In kết quả ra màn hình   
    printOutput(counts)

    ###########################################

    spark.stop()
