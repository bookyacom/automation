deps:
  pkg:
    - installed
    - pkgs:
      - build-essential
      - git
      - wget
      - tcl8.5

redis:
  pkg:
    - installed
    - pkgs:
      - redis-server
  service:
    - running
    - name: redis-server
    - require:
      - pkg: redis
