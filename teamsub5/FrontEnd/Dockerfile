# Step 1: Use the official Python image as the base
FROM tiangolo/uwsgi-nginx-flask:python3.8

# Step 2: Set a working directory
WORKDIR /FrontEnd

# Step 3: Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Step 4.1: Copy the rest of the application files
COPY . . 

# Step 4.2: Git 설치 (경량 이미지에서는 git 설치가 필요할 수 있음)
# RUN apt-get update && apt-get install -y git

# Step 4.3: GitHub 저장소 클론
# RUN git clone https://github.com/username/repository.git .

# Step 5: Expose the port Flask will run on (80 for this example)
EXPOSE 5000

# Step 6: Run the Flask application on 0.0.0.0:80
CMD ["python", "main.py"]