# Suppress error message(s)
$ErrorActionPreference = "SilentlyContinue"
# Clear folder
Remove-Item .\ -Include *.py
Remove-Item .\zapv2 -Recurse 
Remove-Item .\requests -Recurse 
# Download latest scripts
wget https://raw.githubusercontent.com/zaproxy/zaproxy/master/build/docker/zap_common.py -OutFile zap_common.py
wget https://raw.githubusercontent.com/zaproxy/zaproxy/master/build/docker/zap-baseline.py -OutFile zap-baseline.py
# Install requirements
pip install -r requirements.txt
# Copy ZAP2 to local
Copy-Item $env:PY_HOME\Lib\site-packages\zapv2 .\ -Recurse
Copy-Item $env:PY_HOME\Lib\site-packages\requests .\ -Recurse
