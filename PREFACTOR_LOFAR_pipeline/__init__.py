import json
import os
import subprocess
from fabric import Connection
import requests

def give_name():
    jsonfile = give_config()
    name = list(jsonfile.keys())[0]
    return name

def give_version():
    return "0.1"

def give_config():
    json_config_file = os.path.join(os.path.dirname(__file__), "data", "config.json")
    with open(json_config_file) as json_data:
        return json.load(json_data)

def give_argument_names(required=False):
    jsonfile = give_config()
    name = list(jsonfile.keys())[0]
    required = jsonfile[name]["schema"]["required"]
    properties = set(jsonfile[name]["schema"]["properties"].keys())
    if required:
        return required
    else:
        return properties

def run_pipeline(observation, **kargs):
	# Start your pipeline here
    print("===OBSERVATION: " + observation)
    test_cmd = 'xenon scheduler ssh --location localhost exec /bin/hostname'
    cmd_arr = ["xenon", "scheduler", "ssh", "--location", "localhost", "exec", "/bin/hostname"]
#    #print("Running command " + test_cmd)
#    #cmd_out =subprocess.run(test_cmd, stdout=subprocess.STDOUT, text=True).stdout
#    #cmd_out = subprocess.run(cmd_arr, text=True, capture_output=True).stdout
#    #subprocess.run(cmd_arr)
#    cmd_str = "sbatch /var/scratch/madougou/LOFAR/sjob"
#    conn = Connection(host="fs0.das5.cs.vu.nl", user="madougou")
#    out_items = conn.run(cmd_str).stdout.split()
#    job_id = out_items[len(out_items) - 1]
#    return job_id
    url = "http://localhost:8443/jobs"
    headers = {
        "Content-Type": "application/json",
        "api-key": "in1uP28Y1Et9YGp95VLYzhm5Jgd5M1r0CKI7326RHwbVcHGa"
    }
    data = {
        "name": "PREFACTOR CWL Workflow",
        "workflow": "workflow.cwl",
        "input": {}
    }
    res = requests.get(url, headers=headers, data=data)
    return res.status_code
