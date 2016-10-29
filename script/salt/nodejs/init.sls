deps:
  pkg:
    - installed
    - pkgs:
      - build-essential
      - git
      - curl

node:
  cmd:
    - run
    - name: curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
    - unless: node -v
    - require:
      - pkg: deps
    - require_in:
      - pkg: node
  pkg:
    - installed
    - pkgs:
      - nodejs
