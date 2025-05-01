# This is the file that will run when you run the module mallard.
# For now, we want to use the cli version by default, so let's import that and call the run function

import mallard.cli
import sys

# Check for a supported OS. At the moment, we'll support Linux and
# Darwin (MacOS)
if not (sys.platform == "darwin" or sys.platform == "linux"):
    print(f"{sys.platform} is not currently supported. Exiting...")
    exit()

mallard_cli = mallard.cli.CLI()
mallard_cli.run()
