FROM centos:7
MAINTAINER Kazuhisa Hara <kazuhisya@gmail.com>

RUN yum install -y yum-utils rpmdevtools make git epel-release
COPY / /libyrmcds-rpm
WORKDIR /libyrmcds-rpm

RUN yum-builddep -y ./libyrmcds.spec
RUN make rpm
RUN yum install -y \
        --nogpgcheck \
        ./dist/RPMS/x86_64/libyrmcds-[^d.+].* \

CMD ["yc", "version"]

