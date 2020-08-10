FROM python:3.7.8-alpine3.12

LABEL maintainer "lyc8503@foxmail.com"

# 安装依赖
RUN pip3 install --no-cache-dir requests rsa chardet

# 添加文件
RUN mkdir /data
COPY ["bilibili.py", "daily_bonus.py", "/data/"]

ENTRYPOINT ["python3", "/data/daily_bonus.py"]