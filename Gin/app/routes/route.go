package routes

import (
	v1 "webback-go/app/api/v1"

	"github.com/gin-gonic/gin"
)

func RegisterRoutes(router *gin.Engine) {
	v1Group := router.Group("/api/v1")
	{
		v1Group.GET("/ping", v1.PingHandler)
	}
}
