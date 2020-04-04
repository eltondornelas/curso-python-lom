# integrando_qtdesigner_com_pyqt5

"""
# Instalar e remover no Windows
# Instalar Windows (Via PIP)
pip install pyqt5-tools

# Remover Windows (Via PIP)
pip uninstall pyqt5-tools

# ACESSAR NO WINDOWS (Obs.: este caminho poderÃ¡ ser diferente)
# Pasta
explorer %LOCALAPPDATA%\programs\python\python37-32\lib\site-packages\pyqt5_tools\
# Qt Designer
%LOCALAPPDATA%\programs\python\python37-32\lib\site-packages\pyqt5_tools\designer.exe
"""

# Aula - Instalação e primeiro contato com PyQT5
"""
# OBS: esta aula utiliza o arquivo: introducao.py 

# Instalar e remover Linux Ubuntu

# Instalar no Ubuntu
pip install pyqt5
sudo apt-get install qttools5-dev-tools  # QT Designer
 

# Remover Linux Ubuntu
pip uninstall pyqt5
sudo apt purge qttools5-dev-tools -y && sudo apt autoremove -y && sudo apt install -f

"""

# Aula - Criando uma calculadora com PyQT5
"""
# OBS: esta aula utiliza o arquivo: criando_calculadora.py

"""

# Aula - integrando_qtdesigner_com_pyqt5
"""
# por padrão do PyQT5 e do QTDesigner, utiliza-se camelCase

pyuic5 nomearquivo.ui -o nomedestino.py
# conver o arquivo de design em python
"""

# Aula - Adicionando PyQT6 em código Python Antigo
"""
# OBS: essa aula utiliza o diretório: cpfpyqt5

"""