# AVA - Portal

AVA - Portal

```bash

# For BASH
echo "" >> /etc/profile
echo "# AVA Portal" >> /etc/profile
echo "export AP_HOME=/var/dockers/avaportal" >> /etc/profile
source ~/.bashrc

# For ZSH
echo "" >> ~/.zshrc
echo "# AVA Portal" >> ~/.zshrc
echo "export AP_HOME=/var/dockers/avaportal" >> ~/.zshrc
source ~/.zshrc

# Baixe o proejto
mkdir -p /var/dockers
git clone git@github.com:suap-ead/avaportal.git $AP_HOME

# Copie e edite as variáveis de ambiente
cp -r $AP_HOME/confs/examples $AP_HOME/confs/enabled
vim $AP_HOME/confs/enabled/db.env
vim $AP_HOME/confs/enabled/avaportal.env

# Instala o sistema
cd $AP_HOME/bin
./avaportal/migrate
./avaportal/manage createsuperuser

# Sobe o serviço
./avaportal/up

# Se fores fazer um debug
# ./avaportal/debug
```

O serviço estará disponível em http://localhost/ e será parecido com o que se vê abaixo:


![Alt text](screenshot.png?raw=true "Screenshot")