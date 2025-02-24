Clone this repo 
You should run this commands in your terraform directory 
```
terraform plan -out=plan.tfplan
terraform show -json plan.tfplan > aname.json
rm plan.tfplan
# create this directory if you don't have it mkdir ~/depurtfplan/books
mv aname.json ~/depurtfplan/books/
python3 ~/depurtfplan/main.py
```
