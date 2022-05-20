FROM openjdk:11 
WORKDIR /app
COPY spring-boot-app.jar /app
ENV SERVER_PORT 9090
EXPOSE $SERVER_PORT
CMD ["java", "-jar", "spring-boot-app.jar" ]