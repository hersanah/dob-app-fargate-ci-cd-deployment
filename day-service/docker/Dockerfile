FROM public.ecr.aws/docker/library/python:3.11-alpine3.19


# Create directory inside container
RUN mkdir ./day

# Set working directory
WORKDIR /day


# Copy requirements file into /app
COPY ../requirements.txt .


# Install python dependencies
RUN pip install -r requirements.txt


# Copy the rest of the application code
COPY . .


# Document to inform whoever using this Dockerfile, this app is listening to port 80
EXPOSE 80


# Command to run the application
CMD ["python", "day.py"]