# 使用Anaconda來建立環境
> conda create --name WorldFlipperDownloader python=3.7.13

# 進入已建立的Python環境
> activate WorldFlipperDownloader

# 匯入所有安裝的套件
> pip3 install -r requirements.txt

# 匯出所有安裝的套件
> pip3 list --format=freeze > requirements.txt

# 執行
> python ./main.py