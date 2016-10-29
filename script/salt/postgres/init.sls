deps:
  pkg:
    - installed
    - pkgs:
      - build-essential
      - git

postgresql:
  pkg:
    - installed
    - require:
      - pkg: deps
    - pkgs:
      - postgresql
      - postgresql-contrib
      - postgis
      - postgresql-9.3-postgis-2.1
  user:
    - present
    - name: postgres
  cmd:
    - run
    - name: createuser -d -s admin
    - user: postgres
    - require:
      - user: postgresql
      - pkg: postgresql
