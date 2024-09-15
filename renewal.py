import os 
import subprocess
from git import Repo
#---- Global Variables ------
CF_Token = os.environ['CF_Token']
#domain = os.getenv("domain")
def renew_cert() :
    domain = "office.3es-eg.uk"
    Repo.clone_from('https://github.com/3Es-for-smart-solutions/scripts', 'scripts')
    os.chdir("scripts/acme-cert-bot")
    command = "./acme.sh --issue --dns dns_cf --ocsp-must-staple --server letsencrypt  --keylength ec-384 -d %s --dnssleep 120 --days 90 --home '%s'" %(domain,domain)
    result = subprocess.run(command,shell=True)
    if (result.returncode == 0 ):
        cert_path = str("./"+domain + "_ecc/" + domain + ".cer")
        result2 = subprocess.run(["scp",cert_path,"zeyad@127.0.0.0:/home/zeyad/Desktop/" ])
        
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
