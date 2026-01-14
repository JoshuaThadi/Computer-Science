library(MASS)
schools = table(painters$School)
barplot(schools)
pie(schools)
stem(schools)
painters