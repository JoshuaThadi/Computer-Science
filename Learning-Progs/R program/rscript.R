# ----- Q- test of SIGNIFICANT for PROPORTION
# (single proportion Ho : P = Po)

p_hat = 0.65
n = 100
p0 = 0.5

z_score = (p_hat - p0) / sqrt(p0 * (1 - p0) / n)
p_value = 2 * (1 - pnorm(abs(z_score)))

cat("z-score -> ", z_score, "\n")
cat("p_value -> ", p_value, "\n")


# ------ calculate probability based on Normal distribution

n = 10
p = 0.5

prob = dbinom(5, size = n, prob = p)
mean_value = n * p
variance = n * p * (1 - p)

cat("Probability of getting exactly 5 successes in 10 trials : ", prob,"\n")

cat("Mean : ", mean_value, "\n")
cat("Variance : ", variance, "\n")


# ------ Q- t-test for significant of single mean
# population variance beign unknown (Single mean Ho : u = uo)

data = c(10, 12, 14, 8, 11, 9, 13, 7, 10, 11)
mu_0 = 10
result = t.test(data, mu = mu_0)
print(result)


# ------- Q- F-test to compare two variances

group1 = c(23, 25, 28, 22, 21)
group2 = c(18, 20, 19, 17, 21, 23)

result = var.test(group1, group2)
print(result)


# Q- Perform One-way ANOVA

group1 = c(10, 21, 14, 16, 18)
group2 = c(8, 9, 11, 13, 15)
group3 = c(7, 8, 9, 11, 13)

data = data.frame(value = c(group1, group2, group3),
                  group = factor(rep(c("Group1", "Group2", "Group3"),each = 5)))

result = aov(value ~ group, data = data)
summary(result)
t = summary(result)
print(t)


# ------- Q- Perform Two-way ANOVA

group1 = c(10, 12, 14, 16, 18)
group2 = c(8, 9, 11, 13, 15)

result = var.test(group1, group2)
print(result)


# --------- Q- perform sign test

data = c(-1, 2, -3, 4, -5, 6, -7, 8)

binom_test_result = binom.test(sum(data > 0), length(data),
                               p = 0.5, alternative = "two.sided")

print(binom_test_result)

# -------- Kruskal - Wallis test

myData = PlantGrowth
print(myData)

print(levels(myData$group))
myData = PlantGrowth

result = kruskal.test(weight ~ group, data = myData )
print(result)

