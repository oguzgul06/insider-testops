# Insider TestOps — Kubernetes + Selenium Automation Framework

Bu repo Insider TestOps görevi için hazırlanmış tam kapsamlı bir otomasyon mimarisidir.

## İçerik
- Selenium + PyTest testleri
- Kubernetes üzerinde Chrome Node çalıştırma
- Controller pod ile test tetikleme
- Python deploy & test runner
- Docker imajları ve manifestleri

## Docker Build
docker build -t <user>/insider-controller:v1 ./controller
docker build -t <user>/insider-chrome-node:v1 ./chrome-node

## Kubernetes Deploy
kubectl apply -f k8s/controller-deployment.yaml
kubectl apply -f k8s/chrome-deployment.yaml

## Test Çalıştırma
python deploy/deploy_and_run.py 3
