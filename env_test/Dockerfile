FROM alpine
RUN apk update
RUN apk add python3
RUN pip3 install bottle
ADD report.py /
CMD python3 report.py
EXPOSE 80
