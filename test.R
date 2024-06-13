# read tidyverse library
library(tidyverse)

# read a parquet file and print the first 6 rows
df <- read_parquet("data.parquet")
print(head(df))
