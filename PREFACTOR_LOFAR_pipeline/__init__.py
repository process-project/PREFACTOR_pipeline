import json
import os
import subprocess

def give_name():
    jsonfile = give_config()
    name = list(jsonfile.keys())[0]
    return name

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
    test_cmd = 'xenon scheduler ssh --location localhost exec /bin/hostname'
    print("Running command " + test_cmd)
    return subprocess.run(test_cmd, capture_output=True, stdout=subprocess.STDOUT, text=True).returncode
