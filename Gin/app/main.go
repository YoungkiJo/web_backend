package main

import (
	"log"
	"webback-go/app/config"
	"webback-go/app/routes"

	"github.com/gin-gonic/gin"
	"github.com/joho/godotenv"
)

func main() {
	// .env 파일 로드
	if err := godotenv.Load(); err != nil {
		log.Fatal("Error loading .env file")
	}

	// 설정 가져오기
	cfg := config.GetConfig()

	// Gin 라우터 생성
	router := gin.Default()

	// 라우터 등록
	routes.RegisterRoutes(router)

	// 서버 실행
	err := router.Run(cfg.Host + ":" + cfg.Port)
	if err != nil {
		log.Fatalf("Failed to run server: %v", err)
	}
}
