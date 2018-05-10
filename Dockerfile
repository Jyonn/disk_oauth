FROM python:3.6

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY common.py /opt/disk_oauth/
COPY disk_oauth.py /opt/disk_oauth/
COPY error.py /opt/disk_oauth/
COPY qtb.py /opt/disk_oauth/
COPY response.py /opt/disk_oauth/
COPY config.py /opt/disk_oauth/
EXPOSE 5000
WORKDIR /opt/disk_oauth
CMD python disk_oauth.py 5000