gst-launch-1.0 uvch264src device=/dev/video0 initial-bitrate=3000000 average-bitrate=3000000 iframe-period=3000 name=src auto-start=true \
            src.vidsrc ! queue ! video/x-h264,width=1280,height=720,framerate=30/1 ! h264parse ! rtph264pay ! udpsink host=localhost port=5600
