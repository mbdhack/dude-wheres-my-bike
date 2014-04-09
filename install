pps=(

python-dev
python-easy_install
python-pip
python-virtualenv

)

# Loop over apps and install each one with default 'yes' flag
for app in "${apps[@]}"
do
    apt-get install $app -y
done

easy_install pip
pip install virtualenv
virtualenv env
source env/bin/activate
pip install -r requirements.txt

bash run
