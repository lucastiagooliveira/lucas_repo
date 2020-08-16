getwd()
setwd("C:/Users/lucas/Documents/lucastiagooliveira/Study Materials/R_classes")

help("vector")

install.packages("Rtools")
library(dplyr)

6*6

7/2

(4*(6+2))/4
4/0
10^1000 - 10^99

1 > 2

help("for")

for (i in 1:5) print (1:i)

rm(i)

if (1){
  
}else{
  
}

lista = c("laticinios", "frutas", "limpeza")

for (i in lista){
  print(paste(i, "- ok", sep =" "))
}

square = function(x){
  temp = x*x
  return(temp)
}

for (i in 1:10){
  print(square(i))
}

project_price = function(hours, price = 40){
  if (hours > 100){
    return(price * hours * 0.9)
  }else{
    return(price * hours)
  }
}

project_price(101,100)

vetor = 1:5
vetor2 = 5:9

2*vetor
vetor2*vetor

sin(vetor)

sum(vetor)

vetor_text = c("laticinios", "produtos de limpeza", "frutas")

vetor_seq = seq(1, 5, by = 0.1)

vetor_repeticao = rep(1:2, times = 3)

x = c(5,4,9,6,8,9,23,9,9)

sort(x)

table(x)

unique(x)

rev(x)

x[1]
x[-4] #return a vector without this position

x[2:5]
x[-(2:5)]
x[c(1,2,5,7)]

x[x != 9] #subsetting by value

x[x > 7]

vector1 = c(1,2)
vector2 = c(2,4,6,8)

vector1 * vector2 # result = 2  8  6 16

matriz = matrix(1:12, nrow = 3, ncol = 4)
matriz2 = matrix(1:6, nrow = 3, ncol = 4)

matriz[2,] #all values in second row

matriz[,1] #all values in first column

t(matriz)

lista = list(posi1 = 1:5, posi2 = c("a","b",'c'))

sum(lista[1]) #error
sum(lista[[1]]) #working

sum(lista$posi1) #working too (the best way)

df = data.frame(colunaA = 1:3, colunaB = c("a",'b','c'))

head(df)
tail(df)

df[,2] #get second column
df[2,] #get second row
df[2,2]

nrow(df)
ncol(df)

dim(df)

base_rh_csv = read.csv("Base RH.csv", sep = ",")

base_rh_rds = readRDS("Base RH.RDS")

install.packages("openxlsx", dependencies = TRUE)

library(openxlsx) ##load the package

base_rh_xlsx = read.xlsx("Base RH.xlsx")

head(base_rh_csv)
tail(base_rh_csv)

base_rh_fem = base_rh_csv[base_rh_csv$Genero == "Feminino",]

class(base_rh_csv)

summary(base_rh_fem)

library(dplyr)
library(skimr)
library(ggplot2)

install.packages('skimr', dependencies = TRUE)
install.packages("ggplot2", dependencies = TRUE)

skim(base_rh_csv)

ggplot(base_rh_csv) + 
  geom_histogram(mapping = aes(x = SalarioMensal))

base_rh_csv$Satisfacao = as.factor(base_rh_csv$Satisfacao)

ggplot(base_rh_csv, mapping = aes(x = SalarioMensal, colour = Satisfacao))+
  geom_freqpoly(binwidth = 1000)

base_rh_csv %>%
  count(Satisfacao)

ggplot(base_rh_csv, mapping = aes(x = SalarioMensal, y = Satisfacao))+
  geom_boxplot()+
  coord_flip()
y <- list(4:7)

c(1,3,5,7)*y[[1]]

y<-2 
g<-function(x) { x + y } 
f<-function(x){ y <- 1; y^2 + g(x)}
a = c(Inf, 2)
b = c(1,6,7,9,8)
a*b

x <- c(8,9,10)
y <- c(10,2)
x*y
x <- list(5,'a','TRUE',list(3,4,5))

class(x[[3]])

df <- data.frame(a = c(9,8,7), b = c(6, 5, 4), c(3, 2, 1))

df[[2]][[2]]
df$b[[2]]
