@echo off
cd /d "C:\Users\Avinash\Documents\SD\fusion"
start cmd /k "env\Scripts\activate && python facefusion.py run --output-path C:\Users\Avinash\OneDrive\Documents\SD\fusion\output --output-video-preset ultrafast --execution-providers directml --face-mask-types occlusion --execution-thread-count 10 --execution-queue-count 2"