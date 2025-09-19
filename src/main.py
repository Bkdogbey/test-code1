import yaml
from data.process import power, square
from utils import skip_run

# The configuration file
config_path = "configs/config.yml"
config = yaml.load(open(str(config_path)), Loader=yaml.SafeLoader)

with skip_run("skip", "Step 1") as check, check():
    y = square(2)
    print(y)

with skip_run("skip", "Step 2") as check, check():
    y = square(2)
    print(y)

with skip_run("skip", "Step 3") as check, check():
    y = power(4)
    print(y)
