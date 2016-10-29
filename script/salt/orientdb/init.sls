{%- set version = '2.1.5' -%}
{%- set checksum = 'ab474b3903a720728c5e379e8175329b' %}

deps:
  pkg:
    - installed
    - name: openjdk-7-jre-headless

orientdb:
  group:
    - present
  user:
    - present
    - gid: orientdb
    - require:
      - group: orientdb
  archive:
    - extracted
    - name: /opt
    - archive_format: tar
    - tar_options: zxf
    - source_hash: md5={{ checksum }}
    - source: "http://orientdb.com/download.php?file=orientdb-community-{{ version }}.tar.gz"
    - if_missing: /opt/orientdb-community-{{ version }}
    - user: orientdb
    - group: orientdb
    - require:
      - pkg: deps
      - user: orientdb
  file:
    - managed
    - name: /opt/orientdb-community-{{ version }}/config/orientdb-server-config.xml
    - source: salt://orientdb/server.jinja2
    - user: orientdb
    - group: orientdb
    - template: jinja
    - require:
      - archive: orientdb
  service:
    - running
    - enable: True
    - watch:
      - file: /opt/orientdb-community-{{ version }}/bin/orientdb.sh
      - file: /etc/init.d/orientdb
      - file: orientdb
    - require:
      - file: /etc/init.d/orientdb

/opt/orientdb-community-{{ version }}/bin/orientdb.sh:
  file:
    - managed
    - source: salt://orientdb/service.jinja2
    - user: orientdb
    - group: orientdb
    - template: jinja
    - mode: 640
    - context:
      orientdb_user: orientdb
      orientdb_home: /opt/orientdb-community-{{ version }}
    - require:
      - archive: orientdb

/usr/bin/orientdb:
  file:
    - symlink
    - target: /opt/orientdb-community-{{ version }}/bin/console.sh
    - require:
      - archive: orientdb

/etc/init.d/orientdb:
  file:
    - copy
    - source: /opt/orientdb-community-{{ version }}/bin/orientdb.sh
    - force: True
    - mode: 744
    - require:
      - file: /opt/orientdb-community-{{ version }}/bin/orientdb.sh
