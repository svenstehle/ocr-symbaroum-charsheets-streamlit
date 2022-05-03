pytest tests/integration/app --settings-file=tests/visual_testing.py \
    --chromium-arg="force-device-scale-factor=1,headless" --visual_baseline
