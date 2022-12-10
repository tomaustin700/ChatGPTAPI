FROM --platform=amd64 python:3.9-slim
EXPOSE 5000
ADD API.py /

RUN pip install chatgptpy --upgrade
RUN pip install flask
RUN pip install flask_cors

CMD ["python", "./API.py"]