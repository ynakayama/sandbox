df = read.csv("sample_data.csv")

row.names(df) = df[,1]
df = df[,2:8]
head(df)

png("image.png", width = 480, height = 480, pointsize = 12, bg = "white", res = NA)
par(xpd=TRUE)
biplot(prcomp(df, scale=TRUE))
dev.off()

result <- factanal(x = df, factors = 2)
result
1 - result$uniquenesses
