FROM python:3.8
COPY . /root
WORKDIR /root
VOLUME ["/root/static/md", "/root/static/pic", "/root/static/res", "/root/db"]
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
# RUN python3 manage.py migrate

EXPOSE 8000
ENTRYPOINT ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
