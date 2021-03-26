FROM centos:latest
MAINTAINER Siewyan Hoh <siew.yan.hoh@cern.ch>

RUN yum install -y python38 git make 
RUN echo "export PATH=/bin:$PATH" >> /root/.bashrc
RUN pip3.8 install sphinx rinohtype