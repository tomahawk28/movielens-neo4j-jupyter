FROM neo4j:3.4.9

COPY ./download_and_import.sh /
COPY ./headers /data/headers

RUN bash -c "/download_and_import.sh"

ENTRYPOINT ["/sbin/tini", "-g", "--", "/docker-entrypoint.sh"]
CMD ["neo4j"]
