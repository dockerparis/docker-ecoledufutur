FROM ubuntu:14.04

RUN apt-get update

# installation du package
RUN apt-get install -y celestia-gnome sunclock stellarium gpredict python 

# Replace 1000 with your user / group id
RUN export uid=1000 gid=1000 && \
        mkdir -p /home/user && \
        echo "user:x:${uid}:${gid}:User,,,:/home/user:/bin/bash" >> /etc/passwd && \
	echo "user:x:${uid}:" >> /etc/group && \
	echo "user ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/user && \
	chmod 0440 /etc/sudoers.d/user && \
	chown ${uid}:${gid} -R /home/user

ADD controller.py /bin/
ADD packages /var/

USER user
ENV HOME /home/user


EXPOSE 8000/tcp

#CMD /usr/bin/celestia
CMD python /bin/controller.py
