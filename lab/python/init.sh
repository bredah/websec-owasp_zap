# Clear folder
rm -f *.py
# Download latest scripts
wget https://raw.githubusercontent.com/zaproxy/zaproxy/master/build/docker/zap_common.py
wget https://raw.githubusercontent.com/zaproxy/zaproxy/master/build/docker/zap-baseline.py
# Install requirements
pip install -r requirements.txt