FROM debian
RUN apt-get update
RUN apt-get install -y python3
ADD incremental_alloc.py /
CMD python3 /incremental_alloc.py
