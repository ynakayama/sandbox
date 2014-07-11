png("image.png", width = 480, height = 480, pointsize = 12, bg = "white", res = NA)

plot(data$WRAIN, data$LPRICE2, pch=16,
     xlab="収穫前年の10月〜3月の雨量",
     ylab="ワインの価格")

dev.off()
