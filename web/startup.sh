#! /bin/bash
cd /opt/lab/web
pip install -r requirements.txt
pip install icalendar
npm install
bower install --allow-root
python housekeeper_web/web.py