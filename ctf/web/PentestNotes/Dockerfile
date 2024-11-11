FROM openjdk:17-jdk-slim

RUN apt-get update && apt-get install -y maven && rm -rf /var/lib/apt/lists/*

COPY challenge/ /app

WORKDIR /app

# Use Maven to compile the project
RUN mvn clean package

# Copy the flag file and rename it with a random string
COPY flag.txt /
RUN FLAG_NAME=$(head /dev/urandom | tr -dc A-Za-z0-9 | head -c 12) && mv /flag.txt "/${FLAG_NAME}_flag.txt" 

# Use Maven to run the Spring Boot application
CMD ["mvn", "spring-boot:run"]

EXPOSE 8080
