# Development Workflow

## Branching Strategy
We are following `git-flow` branching strategy.
- **Master branch** - Stable release branch with tag
- **Development branch** - Development branch with new features
- **Hotfix branch** - Hotfix branch is a bug fixes on release, it should branch out from master and merged into Master and Development branch
- **Feature branch** - Feature branch is branch where you develop new feature, naming `feature/<%= feature-name %>`
- **Enhancement branch** - Enhancement branch is branch where you updating an existing feature, naming `enhancement/<%= feature-name %>`

## Understanding of folder structure

>TODO

## How to release
1. merge `development` to `master`.
2. create a release on `github` with auto tagging.
