library(ggplot2)
head(iris)


ggplot(data = iris, aes(x = Sepal.Length, y = Sepal.Width)) +
  geom_point() +
  theme_bw()

myplot <- ggplot(data = iris, aes(x = Sepal.Length, y = Sepal.Width))
myplot <- myplot + geom_point()
myplot <- myplot + theme_bw()
myplot


ggplot(data = iris, aes(x = Sepal.Length, y = Sepal.Width)) +
  geom_point(size = 3)

ggplot(data = iris, aes(x = Sepal.Length, y = Sepal.Width)) +
  geom_point(aes(size = Sepal.Length))


ggplot(iris, aes(Sepal.Length, Sepal.Width, color = Species)) +
  geom_point(size = 3)

head(iris)
iris2 <- iris
iris2$location <- rep(c("a", "b", "c"), nrow(iris2)/3)

ggplot(iris2, aes(Sepal.Length, Sepal.Width, color = location)) +
  geom_point(size = 3)



ggplot(iris, aes(Sepal.Length, Sepal.Width, color = Species)) +
  geom_point(aes(shape = Species), size = 3)




d2 <- diamonds[sample(1:dim(diamonds)[1], 1000), ]
ggplot(d2, aes(carat, price, color = color)) + 
  geom_point() + theme_gray()



library(MASS)
ggplot(birthwt, aes(factor(race), bwt)) + geom_boxplot()



h <- ggplot(faithful, aes(x = waiting))
h + geom_histogram(binwidth = 30, colour = "black")



h <- ggplot(faithful, aes(x = waiting))
h + geom_histogram(binwidth = 8, fill = "steelblue",
                   colour = "black")

h + geom_density()

setwd('~/SFSU_bioinfo/ggplot-lecture-master/')


climate <- read.csv("climate.csv", header = T)
head(climate)


ggplot(climate, aes(Year, Anomaly10y)) +
  geom_line()



ggplot(climate, aes(Year, Anomaly10y)) +
  geom_ribbon(aes(ymin = Anomaly10y - Unc10y,
                  ymax = Anomaly10y + Unc10y),
              fill = "blue", alpha = .1) +
  geom_line(color = "steelblue")


ggplot(climate, aes(Year, Anomaly10y)) +
  geom_line(color = "steelblue") +
  geom_ribbon(aes(ymin = Anomaly10y - Unc10y,
                  ymax = Anomaly10y + Unc10y),
              fill = "blue", alpha = 1)

ggplot(climate, aes(Year, Anomaly10y)) +
  geom_ribbon(aes(ymin = Anomaly10y - Unc10y,
                  ymax = Anomaly10y + Unc10y),
              fill = "blue", alpha = 1) +
  geom_line(color = "red")


cplot <- ggplot(climate, aes(Year, Anomaly10y))
cplot <- cplot + geom_line(size = 0.7, color = "black")
cplot <- cplot + geom_line(aes(Year, Anomaly10y + Unc10y), linetype = "dashed", size = 0.7, color = "red")
cplot <- cplot + geom_line(aes(Year, Anomaly10y - Unc10y), linetype = "dashed", size = 0.7, color = "red")
cplot + theme_gray()



ggplot(iris, aes(Species, Sepal.Length)) +
  geom_bar(stat = "identity")


# add error bars
head(iris)
summary(iris)

library(tidyr)
library(dplyr)



iris %>%
  group_by(Species) %>%
  summarise(std.err = sqrt(var(Sepal.Length) / length(Sepal.Length) ), avg=mean(Sepal.Length) ) %>%
  arrange(std.err, avg) -> std.err.tab
std.err.tab <- as.data.frame(std.err.tab)
std.err.tab


ggplot(std.err.tab, aes(Species, avg)) +
  geom_bar(stat = "identity") +
  geom_errorbar(aes(ymin=avg-std.err, ymax=avg+std.err), width=0.2 )



df <- gather(iris, key="variable", value="value", -Species)
head(df)
tail(df)

ggplot(df, aes(Species, value, fill = variable)) +
  geom_bar(stat = "identity")


ggplot(df, aes(Species, value, fill = variable)) +
  geom_bar(stat = "identity", position = "dodge")


ggplot(faithful, aes(waiting)) + geom_density()



ggplot(faithful, aes(waiting)) +
  geom_density(fill = "blue", alpha = 0.1)



ggplot(faithful, aes(waiting)) +
  geom_line(stat = "density")


ggplot(iris, aes(Sepal.Length, Sepal.Width, color = Species)) +
  geom_point() +
  facet_grid(. ~ Species)


ggplot(iris, aes(Sepal.Length, Sepal.Width, color = Species)) +
  geom_point() +
  facet_grid(Species ~ .)



ggplot(iris, aes(Sepal.Length, Sepal.Width, color = Species)) +
  geom_point() +
  facet_wrap( ~ Species)



ggplot(iris, aes(Sepal.Length, Sepal.Width, color = Species)) +
  geom_point(aes(shape = Species), size = 3) +
  geom_smooth(method = "lm")



ggplot(iris, aes(Sepal.Length, Sepal.Width, color = Species)) +
  geom_point(aes(shape = Species), size = 3) +
  geom_smooth(method = "lm") +
  facet_grid(. ~ Species)



