@echo off
echo "Starting script..."
"C:\Users\XYZ\AppData\Local\Programs\Python\Python39\python.exe" "C:\Users\XYZ\Desktop\EdgeScraper\EdgeScraperPc.py"
echo "EdgeScraperPc" completed"
"C:\Users\XYZ\AppData\Local\Programs\Python\Python39\python.exe" "C:\Users\XYZ\Desktop\EdgeScraper\EdgeScraperPhone.py"
echo "EdgeScraperPhone completed"
set year=%date:~6,4%
set month=%date:~3,2%
set day=%date:~0,2%
set dateformatted=%year%-%month%-%day%
echo %dateformatted% >> "C:\Users\XYZ\Desktop\EdgeScraper\tracking.txt"
pause