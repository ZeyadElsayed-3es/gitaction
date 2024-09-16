import os 
import subprocess
from git import Repo
#---- Global Variables ------
CF_Token = os.environ['CF_Token']
domain = os.environ['domain']
def renew_cert() :
    domain = "cloud.3es-eg.uk"
    Repo.clone_from('https://github.com/Neilpang/acme.sh.git', 'acme-cert-bot')
    os.chdir("acme-cert-bot")
    #command = "./acme.sh --issue --dns dns_cf --ocsp-must-staple --server letsencrypt  --keylength ec-384 -d %s --dnssleep 120 --days 90 --home '%s'" %(domain,domain)
    #result = subprocess.run(command,shell=True)
    #if (result.returncode == 0 ):
        #print("Certificate renewed successfully.")
        #cert_path = str("./"+domain + "_ecc/" + domain + ".cer")
        result2 = subprocess.run(["scp -P 22 ","acme.sh","zeyad@office.3es-eg.uk:/home/zeyad/Desktop/" ])
        
#------------the output ----------------
        if (result2.returncode == 0 ):
            print("Certificate renewed and transfared successfully.")
        else:
            print("Failed to transfer certificate.")
            print(result.stderr)
    else:
        print("Failed to renew certificate.")
        print(result.stderr)


renew_cert()
