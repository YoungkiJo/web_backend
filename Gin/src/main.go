package main

import (
	"log"
	"webback-go/app/config"

	"github.com/gin-gonic/gin"
	"github.com/joho/godotenv"
)

func main() {
	// .env 파일 로드 및 설정 가져오기
	if err := godotenv.Load(); err != nil {
		log.Fatal("Error loading .env file")
	}
	cfg := config.GetConfig()

	// Gin 라우터 설정
	router := gin.Default()

	// 서버 실행
	err := router.Run(cfg.Host + ":" + cfg.Port)
	if err != nil {
		log.Fatalf("Failed to run server: %v", err)
	}

}
