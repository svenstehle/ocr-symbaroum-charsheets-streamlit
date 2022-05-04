pytest tests --settings-file=tests/visual_testing.py \
    --chromium-arg="force-device-scale-factor=1,headless" \
    --cov-report=xml --cov
