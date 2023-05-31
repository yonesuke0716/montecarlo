# montecarlo
montecarlo

### 仮想環境の構築
"""
pyenv install 3.11.3
"""
できたか確認(3.11.3があればOK)
"""
pyenv versions
"""
Python3.11.3の下にvirtualenvを作成
"""
pyenv virtualenv 3.11.3 bottle_test
"""
仮想環境を切り替える
"""
pyenv global bottle_test
"""
先頭に(bottle_test)と出ればOK

仮想環境を終了するとき
"""
pyenv global system
"""

仮想環境を削除するとき
"""
pyenv uninstall hoge
"""