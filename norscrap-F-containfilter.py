#Python script using nornir.scrapli send configs from file and
#F filter from nornir.core.filter to filter out a specific host in the host file
#based on multiple data attributes and an MOTD banner to it
import getpass
from nornir import InitNornir
from nornir_scrapli.tasks import send_configs_from_file
from nornir_utils.plugins.functions import print_result
from nornir.core.filter import F
from rich import print as rprint
#Note we are importing F filter from nornir.core.filter

nr = InitNornir(config_file="config.yaml")
password = getpass.getpass()
nr.inventory.defaults.password = password
#above section is initialising nornir and using getpass to prompt the user to enter their password
def banner_push(task):
    task.run(task=send_configs_from_file, name="configuring banner", file="banner4.txt")
#function is going to create the object banner_push to send the details in the file
not_selby = nr.filter(~F(town="selby"))
#above is creating the function called not_selby which is going to use the NOT F filter key "~"" 
#to find all hosts with a different town other than selby in the host file
results = not_selby.run(task=banner_push)
print_result(results)
#now we create the object results based on the output from the function output
#and the task banner_push and print the results