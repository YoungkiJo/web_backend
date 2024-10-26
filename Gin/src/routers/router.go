package routers

import (
	"fmt"
	"log"
	"os"

	"github.com/gin-gonic/gin"
	"github.com/joho/godotenv"
)

func StartSimulation(c *gin.Context) {
	c.JSON(200, gin.H{
		"message": "Hello, world!",
	})
}

func Run() {
	err := godotenv.Load()
	if err != nil {
		log.Fatal("Error loading .env file")
	}

	router := gin.Default()
	router.POST("/start", StartSimulation)

	host := os.Getenv("host")
	port := os.Getenv("port")
	address := fmt.Sprintf("%s:%s", host, port)

	err = router.Run(address)
	if err != nil {
		log.Fatal("Error starting server: ", err)
	}
}
