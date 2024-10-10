package config

import (
	"os"
)

type Config struct {
	Host string
	Port string
}

func GetConfig() *Config {
	return &Config{
		Host: os.Getenv("HOST"),
		Port: os.Getenv("PORT"),
	}
}
