# Use the official image as a parent image. 
FROM python:latest 
# Set the working directory. 
WORKDIR /www 
# Copy the file or directory content from your host to WORKDIR 
COPY www . 
# Run the command inside your image filesystem. 
RUN echo "append something" >> index.html
RUN echo "append something bad again!" >> index.html
# set env that persists at runtime; can be changed by docker run
ENV PORT 8080
# which port the container is listening on at runtime. 
EXPOSE $PORT
# Run the specified command within the container. 
CMD python -m http.server $PORT
