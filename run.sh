#check if can enabled!
dmesg | grep -i '\(can\|spi\)'

uvicorn main:app --host "localhost" --port 8000 --reload 