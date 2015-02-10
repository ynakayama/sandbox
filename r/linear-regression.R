
z <- c( 1, 2, 4, 6, 7, 8, 10, 15 )
x <- c( 0.045, 0.114, 0.215, 0.346, 0.410, 0.520, 0.670, 0.942 )

lm(x~z)
coefficients(summary(lm(x~z)))
summary(lm(x~z-1))
confint(lm(x~z-1))

png("image.png", width = 480, height = 480, pointsize = 12, bg = "white", res = NA)
plot(z, x)
dev.off()
