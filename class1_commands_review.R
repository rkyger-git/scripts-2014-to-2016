# 10/20/2016
# Class 1 commands review

# source
# list.files
# <, *, +
# booleans
# <- assignment

setwd("~/SFSU_bioinfo/worksheets_resources_fall_2016/")

?source
source("simple_source.R")
cor(x, y)

?list.files
list.files()

5 < 3
3 < 5
b <- 1:6
5 <= b

m <- 5 * 5
m
k <- 5 + 5
k

# c() seq()
c(1:5, 7, 10, 15)

?seq
seq(1,20, by=2)
seq(1,20, by=3)
seq(1,20, by=0.5)

# # names and indices for vector elements
n <- seq(2,20, by=2)
n[5]
n[3:5]
n[3,5] # doesn't work!
n[c(3,5)]

names(n)
names(n) <- letters[1:10]
names(n)[5]
names(n)[5] <- "fifth"
names(n)
n
str(n)
v <- seq(2,20, by=2)
str(v)

a <- 10:-2
a + 2

?barplot
mat <- cbind(x,y)
barplot(mat)

sqrt(25)

?sin
sin(5)

?help
help(lapply)
?mean

hist(x)
hist(runif(10000))
?hist

