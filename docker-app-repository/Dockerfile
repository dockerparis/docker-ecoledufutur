
FROM ubuntu:14.04


RUN apt-get -y update

# install package building helpers
RUN apt-get -y --force-yes install pure-ftpd

# install dependancies
RUN apt-get -y build-dep pure-ftpd

# setup ftpgroup and ftpuser
RUN groupadd ftpgroup
RUN useradd -g ftpgroup -d /dev/null -s /etc ftpuser

# startup
CMD /usr/sbin/pure-ftpd -c 30 -C 1 -l puredb:/etc/pure-ftpd/pureftpd.pdb -x -E -j -R &\
	/bin/bash

EXPOSE 21/tcp
