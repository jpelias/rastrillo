#!/bin/bash
git config credential.helper store

git pull



git add .
git commit -m "up"
git push

git config credential.helper store
